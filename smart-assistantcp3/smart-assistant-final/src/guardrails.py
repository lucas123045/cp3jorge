\
import re

class GuardrailSystem:

    def __init__(self):
        self.patterns = [
            r"ignore previous instructions",
            r"forget rules",
            r"jailbreak",
            r"dan mode",
            r"reveal system prompt",
            r"bypass security"
        ]

    def validar_input(self, texto: str):
        if len(texto) > 500:
            return False, "Texto muito longo"

        if re.search(r"[<>\\{\\}]", texto):
            return False, "Caracteres proibidos"

        for pattern in self.patterns:
            if re.search(pattern, texto.lower()):
                return False, f"Prompt injection detectado: {pattern}"

        return True, "OK"

    def validar_output(self, resposta: str):
        termos_proibidos = [
            "system prompt",
            "ignore instructions",
            "internal rules"
        ]

        for termo in termos_proibidos:
            if termo.lower() in resposta.lower():
                return False, f"Saída insegura: {termo}"

        return True, "OK"
