import yaml
import json
import requests
import re
import os

script_dir = os.path.dirname(os.path.abspath(__file__))


def extract_json_from_response(text):
    brace_count = 0
    json_start = None

    for i, char in enumerate(text):
        if char == '{':
            if brace_count == 0:
                json_start = i
            brace_count += 1
        elif char == '}':
            brace_count -= 1
            if brace_count == 0 and json_start is not None:
                json_str = text[json_start:i+1]
                try:
                    return json.loads(json_str)
                except json.JSONDecodeError as e:
                    return {"raw_response": text, "error": f"JSON decode error: {e}"}

    return {"raw_response": text, "error": "No valid JSON object found"}


def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


def load_prompt_template(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def query_local_ai(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt},
        stream=True
    )
    response.raise_for_status()

    full_response = ""
    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))
            if "response" in data:
                full_response += data["response"]

    return full_response.strip()


def main():
    input_yaml = os.path.join(script_dir, '../projects.yaml')
    output_json = os.path.join(script_dir, 'ai_suggestions.json')
    prompt_template_path = os.path.join(script_dir, 'prompt.md')

    data = load_yaml(input_yaml)
    projects = data.get('projects', [])
    prompt_template = load_prompt_template(prompt_template_path)

    suggestions = {}

    for project in projects[30:]:  # debug purpose, process only a subset
        project_name = project.get('name', 'unknown')
        print(f"Processing: {project_name}")

        # Convert the project dict to a YAML-formatted string
        project_yaml = yaml.dump([project], sort_keys=False)

        # Insert the YAML into the prompt template
        prompt = f"{prompt_template}\n\n## 🔍 Project to Validate\n```yaml\n{project_yaml}```"

        try:
            ai_response = query_local_ai(prompt)

            parsed_response = extract_json_from_response(ai_response)

            suggestions[project_name] = {
                "input": project,
                "ai_suggestion": parsed_response
            }
        except requests.RequestException as e:
            print(f"Error querying local AI for {project_name}: {e}")
            suggestions[project_name] = {
                "input": project,
                "ai_suggestion": {"error": str(e)}
            }

        break  # debug purpose, only process the first project

    with open(output_json, 'w') as file:
        json.dump(suggestions, file, indent=4)

    print(f"AI suggestions saved to {output_json}")


if __name__ == "__main__":
    main()
