import re

class GuardrailSystem:

    def __init__(self):
        self.patterns = [
            r"ignore previous instructions",
            r"forget the rules",
            r"jailbreak",
            r"DAN mode",
            r"reveal prompt",
            r"system prompt"
        ]

    def validar_input(self, texto):

        if len(texto) > 500:
            return False, "Texto muito grande"

        if re.search(r"[<>]", texto):
            return False, "Caracteres proibidos"

        for pattern in self.patterns:
            if re.search(pattern, texto, re.IGNORECASE):
                return False, f"Ataque detectado: {pattern}"

        return True, "OK"

    def validar_output(self, resposta):

        termos_proibidos = [
            "system prompt",
            "ignore instructions"
        ]

        for termo in termos_proibidos:
            if termo.lower() in resposta.lower():
                return False, "Possível vazamento"

        return True, "OK"
