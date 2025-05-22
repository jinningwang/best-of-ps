import ollama
import time
import json
import os
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def get_model_info(model_name: str) -> str:
    """
    Fetch detailed information about a specified model from Ollama.

    If detailed information is unavailable, returns the model name with a common tag.

    Parameters
    ----------
    model_name : str
        The name (and optional tag) of the model to query, e.g., 'mistral', 'qwen:7b'.

    Returns
    -------
    str
        A string describing the model, e.g., 'mistral:latest (digest: abc123...)'.

    Notes
    -----
    If the model is not found or an error occurs, the function returns the provided model name
    with a generic tag if no specific tag was given (e.g., 'model_name:latest').
    """
    try:
        models = ollama.list()["models"]
        for m in models:
            # Check if the full model name (e.g., 'mistral:latest') or just the base name matches
            if m['name'] == model_name or m['name'].startswith(f"{model_name}:"):
                # Not always present, name usually has tag
                tag = m.get('tag', 'latest')
                digest = m.get('digest', '')
                # Use the full name with tag from ollama.list()
                info = m['name']
                if digest:
                    info += f" (digest: {digest[:12]})"
                return info
        # If the specific tag wasn't found, try to be helpful if base name was given
        if ':' not in model_name:
            return f"{model_name}:latest (not found exactly, defaulting)"
        return f"{model_name} (not found)"  # Model with specific tag not found
    except Exception as e:
        logger.warning(
            f"Could not fetch detailed model info for {model_name}: {e}")
        return f"{model_name} (info unavailable)"


def chat_with_ollama_model_json_output(prompt: str, model_to_use: str) -> str:
    """
    Interacts with a specified local Ollama model and returns
    the response structured as a JSON string.

    Parameters
    ----------
    prompt : str
        The user's query or input to the LLM.
    model_to_use : str
        The name (and optional tag) of the Ollama model to use, e.g., 'mistral', 'qwen:4b'.

    Returns
    -------
    str
        A JSON string containing model info, query time, running time, query, and AI response.
    """
    model_info_str = get_model_info(model_to_use)

    start_time = time.time()

    try:
        response = ollama.chat(
            model=model_to_use,  # This is where the model is specified
            messages=[{'role': 'user', 'content': prompt}],
            options={
                'temperature': 0.3,       # Lower for less creativity, more coherence
                'top_k': 20,              # Consider fewer top tokens
                'top_p': 0.7,             # Nucleus sampling to stay focused
                'repeat_penalty': 1.2,    # Penalize repetition
                # Max tokens to generate (added this back, it's good for controlling response length)
                'num_predict': 1024
            }
        )
        ai_raw_response_content = response['message']['content']
    except ollama.ResponseError as e:
        ai_raw_response_content = f"Error: {e.error}"
        logger.error(f"Ollama Response Error: {e.error}")
    except Exception as e:
        ai_raw_response_content = f"An unexpected error occurred: {e}"
        logger.error(f"Unexpected Error during chat: {e}")

    end_time = time.time()
    running_time = end_time - start_time

    output_data = {
        "model": model_info_str,
        "query_time": datetime.now().isoformat(),
        "running_time_seconds": round(running_time, 4),
        "query": prompt,
        "ai_raw_response": ai_raw_response_content
    }

    return json.dumps(output_data, indent=2)


if __name__ == "__main__":
    # --- Configuration ---
    # Change this to the model you want to use.
    # Make sure you have pulled this model first, e.g., 'ollama pull qwen3:4b'
    # or 'ollama pull mistral'.
    TARGET_MODEL = 'qwen3:4b'  # <--- CHANGE THIS TO YOUR DESIRED MODEL

    OUTPUT_DIRECTORY = "output"  # Directory to save JSON logs
    # --- End Configuration ---

    logger.info(
        f"Starting chat with {TARGET_MODEL} (local via Ollama). Type 'exit', 'quit', or '/bye' to end.")
    logger.info(
        f"Output will be in JSON format, saved to '{OUTPUT_DIRECTORY}'.")

    # Ensure output directory exists
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir_path = os.path.join(script_dir, OUTPUT_DIRECTORY)
    os.makedirs(output_dir_path, exist_ok=True)

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in ('exit', 'quit', '/bye'):
            break

        json_response = chat_with_ollama_model_json_output(
            user_input, model_to_use=TARGET_MODEL)

        # Format date for filename
        now = datetime.now()
        date_str = now.strftime("%Y%m%d")

        # Find next available number for today's file
        existing_files = [
            f for f in os.listdir(output_dir_path)
            if f.startswith(f"{date_str}_") and f.endswith(".json")
        ]
        numbers = []
        for fname in existing_files:
            try:
                # Extract the number between date and .json
                num_str = fname[len(date_str) + 1: -5]
                if num_str.isdigit():
                    numbers.append(int(num_str))
            except ValueError:
                continue  # Skip files that don't match the expected naming convention

        next_number = max(numbers, default=0) + 1

        filename = f"{date_str}_{next_number}.json"
        filepath = os.path.join(output_dir_path, filename)

        try:
            with open(filepath, "w") as f:
                f.write(json_response)
            logger.info(f"Saved JSON output to: {filepath}")
        except IOError as e:
            logger.error(f"Failed to save output to {filepath}: {e}")

        # Only show the "ai_raw_response" field from the JSON output for immediate feedback
        try:
            ai_response = json.loads(json_response).get(
                "ai_raw_response", "Error: AI response not found.")
        except json.JSONDecodeError:
            ai_response = "Error: Could not parse JSON response."

        logger.info(
            "\n--- AI Raw Response ---\n%s\n------------------------\n", ai_response)
