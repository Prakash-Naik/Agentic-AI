import subprocess
import prompt_building


def call_llm(prompt: str) -> str:
    response = subprocess.run(
        ["ollama", "run", "phi3"],
        input=prompt.encode(),
        capture_output=True
    )
    return response.stdout.decode().strip()

#print(call_llm("What is the capital of France?"))