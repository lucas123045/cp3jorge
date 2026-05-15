import json
from src.llm_client import LLMClient
from src.schemas import (
    ClassificacaoSchema,
    ProcessamentoSchema,
    RespostaSchema
)

from src.prompts import (
    CLASSIFICACAO_PROMPT,
    PROCESSAMENTO_PROMPT,
    RESPOSTA_PROMPT
)

class AssistantChain:

    def __init__(self):
        self.llm = LLMClient()

    def etapa1_classificar(self, texto):

        prompt = CLASSIFICACAO_PROMPT.format(texto=texto)

        resposta = self.llm.gerar(prompt)

        data = json.loads(resposta)

        return ClassificacaoSchema(**data)

    def etapa2_processar(self, classificacao, texto):

        prompt = PROCESSAMENTO_PROMPT.format(
            tipo=classificacao.tipo,
            texto=texto
        )

        resposta = self.llm.gerar(prompt)

        data = json.loads(resposta)

        return ProcessamentoSchema(**data)

    def etapa3_responder(self, dados):

        prompt = RESPOSTA_PROMPT.format(dados=dados)

        resposta = self.llm.gerar(prompt)

        data = json.loads(resposta)

        return RespostaSchema(**data)

    def executar(self, texto):

        etapa1 = self.etapa1_classificar(texto)

        etapa2 = self.etapa2_processar(etapa1, texto)

        etapa3 = self.etapa3_responder(etapa2)

        return etapa3.model_dump()
