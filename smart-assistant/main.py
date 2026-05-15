import sys
from src.chain import AssistantChain
from src.guardrails import GuardrailSystem
from src.evaluator import run_evaluation

chain = AssistantChain()
guard = GuardrailSystem()

if "--eval" in sys.argv:
    run_evaluation()
    exit()

print("=== Smart Assistant ===")

while True:
    texto = input("Usuário: ")

    if texto.lower() == "sair":
        break

    safe, motivo = guard.validar_input(texto)

    if not safe:
        print(f"Bloqueado: {motivo}")
        continue

    resultado = chain.executar(texto)

    safe_out, motivo_out = guard.validar_output(resultado["resposta"])

    if not safe_out:
        print(f"Resposta bloqueada: {motivo_out}")
        continue

    print("\nAssistente:")
    print(resultado["resposta"])
