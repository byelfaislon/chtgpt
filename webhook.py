import openai
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuração da API Key da OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# ID da sua assistente personalizada
ASSISTANT_ID = "asst_iUPDzqTfX2tdSh1vvTc5joKg"

@app.route('/webhook', methods=['POST'])
def webhook():
    # Recebe a mensagem do usuário enviada pelo webhook
    data = request.json
    user_message = data.get('message', '')

    # Envia a mensagem para a Assistente personalizada no GPT-4
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Usando o modelo GPT-4
        messages=[
            {"role": "user", "content": user_message}
        ],
        assistant_id=ASSISTANT_ID  # ID da sua assistente personalizada
    )

    # Extrai a resposta gerada pela Assistente
    reply = response['choices'][0]['message']['content']

    # Retorna a resposta em formato JSON
    return jsonify({"reply": reply})

if __name__ == '__main__':
    # Define o host e a porta para o Flask
    app.run(host='0.0.0.0', port=5000)

