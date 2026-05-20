import json
import pandas as pd
from src.chain import AssistantChain
from src.guardrails import GuardrailSystem

class Evaluator:

    def __init__(self):
        self.chain = AssistantChain()
        self.guard = GuardrailSystem()

    def executar_avaliacao(self):
        with open("data/test_dataset.json", "r", encoding="utf-8") as f:
            testes = json.load(f)

        resultados = []

        for item in testes:
            texto = item["texto"]

            safe, motivo = self.guard.validar_input(texto)

            if safe:
                resposta = self.chain.executar(texto)

                resultados.append({
                    "texto": texto,
                    "status": "OK",
                    "tipo": resposta
                })
            else:
                resultados.append({
                    "texto": texto,
                    "status": "BLOQUEADO",
                    "motivo": motivo
                })

        df = pd.DataFrame(resultados)
        df.to_csv("output/eval_results.csv", index=False)

        print("Avaliação concluída.")
