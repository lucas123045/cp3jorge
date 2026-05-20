import os
from dotenv import load_dotenv
import ollama

load_dotenv()

MODEL = os.getenv("OLLAMA_MODEL", "gpt-oss:120b")

class LLMClient:
    def gerar(self, prompt: str) -> str:
        resposta = ollama.chat(
            model=MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return resposta["message"]["content"]
