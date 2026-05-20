from src.schemas import (
    ClassificacaoSchema,
    ProcessamentoSchema,
    RespostaSchema
)

class AssistantChain:

    def etapa1_classificar(self, texto):
        texto_lower = texto.lower()

        if "problema" in texto_lower or "erro" in texto_lower:
            tipo = "reclamacao"
            urgencia = "alta"
        elif "como" in texto_lower or "o que" in texto_lower:
            tipo = "duvida"
            urgencia = "media"
        elif "parabéns" in texto_lower or "gostei" in texto_lower:
            tipo = "elogio"
            urgencia = "baixa"
        else:
            tipo = "sugestao"
            urgencia = "media"

        resultado = {
            "tipo": tipo,
            "urgencia": urgencia,
            "tema": "geral"
        }

        return ClassificacaoSchema(**resultado)

    def etapa2_processar(self, classificacao, texto):
        if classificacao.tipo == "reclamacao":
            dados = {
                "dados_extraidos": {
                    "problema": texto
                },
                "analise": "Usuário relatou um problema.",
                "sentimento": "negativo"
            }

        elif classificacao.tipo == "duvida":
            dados = {
                "dados_extraidos": {
                    "duvida": texto
                },
                "analise": "Usuário possui uma dúvida.",
                "sentimento": "neutro"
            }

        elif classificacao.tipo == "elogio":
            dados = {
                "dados_extraidos": {
                    "elogio": texto
                },
                "analise": "Usuário enviou elogio.",
                "sentimento": "positivo"
            }

        else:
            dados = {
                "dados_extraidos": {
                    "sugestao": texto
                },
                "analise": "Usuário enviou sugestão.",
                "sentimento": "neutro"
            }

        return ProcessamentoSchema(**dados)

    def etapa3_responder(self, processamento):
        resposta = {
            "resposta": f"Solicitação processada com sucesso. Análise: {processamento.analise}",
            "confianca": "alta",
            "acao_sugerida": "Acompanhar solicitação"
        }

        return RespostaSchema(**resposta)

    def executar(self, texto):
        etapa1 = self.etapa1_classificar(texto)
        etapa2 = self.etapa2_processar(etapa1, texto)
        etapa3 = self.etapa3_responder(etapa2)

        return etapa3.model_dump()
