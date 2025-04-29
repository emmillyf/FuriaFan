import openai
import re
import os
from dotenv import load_dotenv

load_dotenv()

AI_API_KEY = os.getenv('AI_API_KEY')
if not AI_API_KEY:
    raise ValueError("Chave da GenAI não encontrada! Verifique seu arquivo .env")

openai.api_key = AI_API_KEY
print("Chave carregada:", AI_API_KEY)

def gerar_pergunta():
    prompt = (
        """Você é um bot de quiz sobre a FURIA CS2. Sempre gere perguntas **diferentes** sobre:
            - Jogadores atuais: FalleN, yuurih, KSCERATO, skullz, chelo(reserva), YEKINDAR.
            - Eventos de 2024-2025.
            - Estratégias, estatísticas ou curiosidades.

        Modelo do quiz:
        Pergunta: [ ]
        A) [Alternativa A]
        B) [Alternativa B]
        C) [Alternativa C]
        D) [Alternativa D]
        Resposta correta: [Apenas UMA letra (A-D)]

        REGRAS:
        - Não repita perguntas sobre o mesmo jogador, varie entre todos os jogadores do time.
        - Apenas 1 pergunta por resposta.
        - NUNCA repita as mesmas perguntas.
        - Nada de "nenhuma das anteriores".
        - Garanta que a resposta esteja entre as alternativas"""
    )

    texto = ""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4.1-mini", 
            store=True,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        texto = response.choices[0].message.content.strip()

        if "Pergunta:" not in texto:
            raise ValueError("Formato de resposta inválido - falta 'Pergunta:'")

        texto = texto.split("Pergunta:")[1].strip()
        texto = "Pergunta:" + texto

        match_pergunta = re.search(r"Pergunta:\s*(.*?)(?=\n\s*[A-D]\))", texto, re.DOTALL)
        if not match_pergunta:
            raise ValueError(f"Não foi possível extrair a pergunta do texto:\n{texto}")
        pergunta = match_pergunta.group(1).strip()

        bloco_alternativas_match = re.search(r"(A\).*?)(?=Resposta correta:)", texto, re.DOTALL)
        if not bloco_alternativas_match:
            raise ValueError(f"Não foi possível encontrar o bloco de alternativas:\n{texto}")
        bloco_alternativas = bloco_alternativas_match.group(1).strip()
        alternativas_list = re.findall(r"([A-D])\)\s*(.*?)(?=\n\s*[A-D]\)|$)", bloco_alternativas, re.DOTALL)
        alternativas = {match[0]: match[1].strip() for match in alternativas_list}

        match_resposta = re.search(r"Resposta correta:\s*([A-D])", texto)
        if not match_resposta:
            raise ValueError(f"Não foi possível extrair a resposta correta:\n{texto}")
        resposta = match_resposta.group(1).upper()

        if len(alternativas) != 4:
            raise ValueError(f"Devem haver 4 alternativas. Encontradas: {len(alternativas)}. Alternativas: {alternativas}. Texto completo:\n{texto}")
        if resposta not in alternativas:
            raise ValueError(f"A resposta correta '{resposta}' não está entre as alternativas fornecidas: {list(alternativas.keys())}. Texto completo:\n{texto}")

        return {
            "pergunta": pergunta,
            "alternativas": alternativas,
            "resposta_correta": resposta
        }

    except Exception as e:
        error_message = f"Erro ao gerar/processar pergunta: {str(e)}"
        if texto:
            error_message += f"\nResposta da IA:\n{texto}"
        raise Exception(error_message)