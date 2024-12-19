import openai
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuração da API Key da OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/webhook', methods=['POST'])
def webhook():
    # Recebe a mensagem do usuário enviada pelo webhook
    data = request.json
    user_message = data.get('message', '')

    try:
        # Envia a mensagem para o modelo GPT-4
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um assistente virtual amigável."},
                {"role": "user", "content": user_message}
            ],
        )

        # Extrai a resposta gerada
        reply = response['choices'][0]['message']['content']

        # Retorna a resposta gerada
        return jsonify({"reply": reply})

    except Exception as e:
        # Retorna o erro em caso de falha
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Define o host e a porta para o Flask
    app.run(host='0.0.0.0', port=5000)
