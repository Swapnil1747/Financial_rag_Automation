import requests

def generate_ollama(model: str, prompt: str, system: str = "", temperature: float = 0.2) -> str:
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "system": system,
        "options": {"temperature": temperature}
    }
    resp = requests.post("http://localhost:11434/api/generate", json=payload)
    resp.raise_for_status()
    return resp.json().get("response", "").strip()
