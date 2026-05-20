from src.chain import AssistantChain
from src.guardrails import GuardrailSystem
from src.evaluator import Evaluator
import argparse

def run_interactive():
    guard = GuardrailSystem()
    chain = AssistantChain()

    print("Smart Assistant iniciado. Digite 'sair' para encerrar.")

    while True:
        texto = input("\nVocê: ")

        if texto.lower() == "sair":
            break

        safe, motivo = guard.validar_input(texto)

        if not safe:
            print(f"Bloqueado: {motivo}")
            continue

        resposta = chain.executar(texto)

        output_ok, motivo_output = guard.validar_output(str(resposta))

        if not output_ok:
            print(f"Resposta bloqueada: {motivo_output}")
            continue

        print("\nAssistente:")
        print(resposta)

def run_evaluation():
    evaluator = Evaluator()
    evaluator.executar_avaliacao()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--eval", action="store_true")

    args = parser.parse_args()

    if args.eval:
        run_evaluation()
    else:
        run_interactive()
