from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Configuração da API Key da OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    user_message = data.get('message', '')

    # Enviar mensagem do usuário para o ChatGPT
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um assistente virtual amigável."},
            {"role": "user", "content": user_message}
        ]
    )

    # Retornar a resposta do ChatGPT
    reply = response['choices'][0]['message']['content']
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
