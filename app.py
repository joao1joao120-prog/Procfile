import os
from flask import Flask

# 1. Cria a aplicação Flask
app = Flask(__name__)

# 2. Define a rota principal
@app.route('/')
def meu_servico_principal():
    # A linha 'return' deve ter indentação (espaços)
    return "O código Python finalmente migrou e está online!"

# 3. Bloco de inicialização com compatibilidade de servidor
if __name__ == '__main__':
    # As próximas duas linhas devem ter indentação (espaços)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
