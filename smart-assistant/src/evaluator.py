import json
import pandas as pd
import matplotlib.pyplot as plt

from src.chain import AssistantChain
from src.guardrails import GuardrailSystem

chain = AssistantChain()
guard = GuardrailSystem()


def run_evaluation():

    with open("data/test_dataset.json", "r", encoding="utf-8") as f:
        testes = json.load(f)

    with open("data/attack_dataset.json", "r", encoding="utf-8") as f:
        ataques = json.load(f)

    resultados = []

    corretos = 0

    for item in testes:

        texto = item["texto"]

        resultado = chain.executar(texto)

        if item["tipo_esperado"] in resultado["resposta"]:
            corretos += 1

        resultados.append({
            "texto": texto,
            "resultado": resultado["resposta"]
        })

    bloqueados = 0

    for ataque in ataques:

        safe, _ = guard.validar_input(ataque["texto"])

        if not safe:
            bloqueados += 1

    accuracy = corretos / len(testes)
    taxa_bloqueio = bloqueados / len(ataques)

    df = pd.DataFrame(resultados)

    df.to_csv("output/eval_results.csv", index=False)

    plt.figure(figsize=(6,4))
    plt.bar(["Accuracy", "Bloqueio"], [accuracy, taxa_bloqueio])
    plt.savefig("output/graficos/metricas.png")

    print("Avaliação concluída")
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Bloqueio: {taxa_bloqueio:.2f}")