# Smart Assistant - FIAP CP03

Projeto desenvolvido para o Checkpoint 03 da FIAP.

## Tecnologias
- Python 3.10+
- Ollama API
- Pydantic
- Pandas
- Matplotlib
- Tiktoken

## Instalação

```bash
pip install -r requirements.txt
```

## Configuração
Instale o Ollama e rode:

```bash
ollama run gpt-oss:120b
```

## Execução

Modo interativo:

```bash
python main.py
```

Modo avaliação:

```bash
python main.py --eval
```
