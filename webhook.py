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
        # Nova chamada compatível com a versão recente da API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um assistente virtual amigável."},
                {"role": "user", "content": user_message},
            ],
            temperature=0.7,  # Controle de criatividade (0.0 a 1.0)
        )
        
        # Extrai a resposta gerada pelo modelo
        reply = response['choices'][0]['message']['content']
        return jsonify({"reply": reply})
    except openai.error.OpenAIError as e:
        # Tratamento de erros da API OpenAI com logs detalhados
        print(f"Erro na API OpenAI: {e}")
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        # Tratamento genérico de outros erros
        print(f"Erro inesperado: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
