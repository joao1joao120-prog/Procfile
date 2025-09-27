# app.py

import os
from flask import Flask

# 1. Cria a aplicação Flask
app = Flask(__name__)

# 2. Define a rota principal que o servidor vai responder
@app.route('/')
def meu_servico_principal():
    # Mensagem exibida no navegador
    return "O código Python migrou sozinho e está online com sucesso!"

# 3. Bloco de inicialização: ajustado para ser compatível com o servidor
if __name__ == '__main__':
    # Lê a porta que o servidor de hospedagem fornece, ou usa 5000 localmente
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)