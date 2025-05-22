"""
Module to validate and suggest updates for projects.
"""

import yaml
import json
import requests

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def check_pypi(package_name):
    response = requests.get(f"https://pypi.org/pypi/{package_name}/json")
    return response.status_code == 200

def check_conda(package_name):
    response = requests.get(f"https://anaconda.org/conda-forge/{package_name}")
    return response.status_code == 200

def suggest_updates(projects):
    suggestions = {}
    for project in projects:
        name = project.get('name')
        github_id = project.get('github_id', '').lower()
        pypi_id = project.get('pypi_id')
        conda_id = project.get('conda_id')
        labels = project.get('labels', [])
        sponsorship = project.get('sponsorship')

        suggestion = {}

        # Check PyPI ID
        if not pypi_id and check_pypi(name.lower()):
            suggestion['pypi_id'] = name.lower()

        # Check Conda ID
        if not conda_id and check_conda(name.lower()):
            suggestion['conda_id'] = f"conda-forge/{name.lower()}"

        # Suggest labels
        if 'gha' not in labels and github_id:
            suggestion.setdefault('labels', []).append('gha')
        if 'pypi' not in labels and pypi_id:
            suggestion.setdefault('labels', []).append('pypi')
        if 'conda' not in labels and conda_id:
            suggestion.setdefault('labels', []).append('conda')
        if 'jupyter' not in labels and 'jupyter' in project.get('description', '').lower():
            suggestion.setdefault('labels', []).append('jupyter')

        # Suggest sponsorship
        if not sponsorship:
            if 'curent' in github_id or 'university' in github_id:
                suggestion['sponsorship'] = 'university'
            elif 'nrel' in github_id or 'lanl' in github_id:
                suggestion['sponsorship'] = 'lab'
            elif 'rte' in github_id:
                suggestion['sponsorship'] = 'forprofit'
            elif 'volunteer' in github_id:
                suggestion['sponsorship'] = 'volunteer'

        if suggestion:
            suggestions[name] = suggestion

    return suggestions

def main():
    input_yaml = 'projects.yaml'
    output_json = 'suggestions.json'

    projects = load_yaml(input_yaml)
    suggestions = suggest_updates(projects)
    save_json(suggestions, output_json)

    print(f"Suggestions saved to {output_json}")

if __name__ == "__main__":
    main()
