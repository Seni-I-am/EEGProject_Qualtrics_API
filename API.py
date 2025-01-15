#pip install flask

from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint para receber o e-mail e limpar os dados
@app.route('/reset-email', methods=['POST'])
def reset_email():
    # Receber dados do Qualtrics
    data = request.json
    email = data.get('email', '')

    # Aqui você pode salvar o e-mail ou realizar alguma ação
    print(f"Email recebido: {email}")

    # Responder ao Qualtrics
    return jsonify({
        "success": True,
        "message": "O e-mail foi processado com sucesso."
    })

if __name__ == '__main__':
    # Rodar o servidor na porta 5000
    app.run(host='0.0.0.0', port=5000)

##Endereço: http://127.0.0.1:5000/reset-email
