import os
import ollama
from dotenv import load_dotenv

load_dotenv()

MODEL = os.getenv("OLLAMA_MODEL", "gpt-oss:120b")

class LLMClient:

    def gerar(self, prompt):
        response = ollama.chat(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]
