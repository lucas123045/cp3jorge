CLASSIFICACAO_PROMPT = """
Você é um classificador inteligente.

Classifique a solicitação do usuário.

Retorne APENAS JSON.

Texto:
{texto}

Formato:
{{
  "tipo": "reclamacao|duvida|elogio|sugestao",
  "urgencia": "alta|media|baixa",
  "tema": "tema principal"
}}
"""

PROCESSAMENTO_PROMPT = """
Você está processando uma solicitação.

TIPO: {tipo}
TEXTO: {texto}

Se for reclamação:
- extraia problema
- identifique sentimento

Se for dúvida:
- responda de forma educativa

Se for elogio:
- agradeça

Retorne JSON.
"""

RESPOSTA_PROMPT = """
Você é Ana, especialista sênior de suporte.

Siga a receita:
1. Entenda
2. Responda
3. Oriente
4. Seja empática

Dados:
{dados}

Retorne JSON:
{{
  "resposta": "...",
  "confianca": "alta|media|baixa",
  "acao_sugerida": "..."
}}
"""