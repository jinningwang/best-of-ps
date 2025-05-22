import ollama
import time
import json
import os
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


def get_model_info(model_name):
    """
    Fetch detailed information about a specified model from Ollama.

    If detailed information is unavailable, returns the model name with the ':latest' tag.

    Parameters
    ----------
    model_name : str
        The name of the model to query.

    Returns
    -------
    str
        A string describing the model, e.g., 'mistral:latest (digest: abc123...)'.

    Notes
    -----
    If the model is not found or an error occurs, the function returns the model name with the ':latest' tag.
    """
    try:
        # List all models and find the one matching model_name (with or without tag)
        models = ollama.list()["models"]
        for m in models:
            # m['name'] might be 'mistral:latest' or 'mistral:7b'
            if m['name'].startswith(model_name):
                tag = m.get('tag', 'latest')
                digest = m.get('digest', '')
                info = f"{m['name']}"
                if digest:
                    info += f" (digest: {digest[:12]})"
                return info
        # If not found, return with ':latest'
        return f"{model_name}:latest"
    except Exception as e:
        logger.warning(
            f"Could not fetch detailed model info for {model_name}: {e}")
        return f"{model_name}:latest"


def chat_with_mistral_json_output(prompt: str) -> str:
    """
    Interacts with the local Mistral model via Ollama and returns
    the response structured as a JSON string.
    """
    model_name_used = 'mistral'  # Define the model name here
    model_info_str = get_model_info(model_name_used)

    start_time = time.time()

    try:
        response = ollama.chat(
            model=model_name_used,
            messages=[{'role': 'user', 'content': prompt}],
            options={
                # --- Hyperparameters for Factual/Reality Checking ---
                'temperature': 0.3,       # Lower for less creativity, more coherence
                'top_k': 20,              # Consider fewer top tokens
                'top_p': 0.7,             # Nucleus sampling to stay focused
                'repeat_penalty': 1.2,    # Penalize repetition
                # 'num_predict': 256        # Max tokens to generate
            }
        )
        ai_raw_response_content = response['message']['content']
    except ollama.ResponseError as e:
        ai_raw_response_content = f"Error: {e.error}"
        print(f"Ollama Error: {e.error}")
    except Exception as e:
        ai_raw_response_content = f"An unexpected error occurred: {e}"
        print(f"Unexpected Error: {e}")

    end_time = time.time()
    running_time = end_time - start_time

    output_data = {
        "model": model_info_str,
        "query_time": datetime.now().isoformat(),
        # Round for readability
        "running_time_seconds": round(running_time, 4),
        "query": prompt,
        "ai_raw_response": ai_raw_response_content
    }

    return json.dumps(output_data, indent=2)  # Use indent for pretty printing


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s: %(message)s')
    logger.info("Chatting with Mistral (local via Ollama). Type 'exit' to quit.")
    logger.info("Output will be in JSON format.")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in ('exit', 'quit', '/bye'):
            break

        json_response = chat_with_mistral_json_output(user_input)
        # Determine output directory relative to script location
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(script_dir, "output")
        os.makedirs(output_dir, exist_ok=True)

        # Format date
        now = datetime.now()
        date_str = now.strftime("%Y%m%d")

        # Find next available number for today's file
        existing = [
            fname for fname in os.listdir(output_dir)
            if fname.startswith(f"{date_str}_") and fname.endswith(".json")
        ]
        numbers = [
            int(fname[len(date_str)+1:-5]) for fname in existing
            if fname[len(date_str)] == '_' and fname[-5:] == ".json" and fname[len(date_str)+1:-5].isdigit()
        ]
        next_number = max(numbers, default=0) + 1

        filename = f"{date_str}_{next_number}.json"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w") as f:
            f.write(json_response)
        logging.info(f"Saved JSON output to: {filepath}")
        # Only show the "ai_raw_response" field from the JSON output
        try:
            ai_response = json.loads(json_response).get("ai_raw_response", "")
        except Exception:
            ai_response = ""
        logging.info(
            "\n--- AI Raw Response ---\n%s\n------------------------\n", ai_response)
