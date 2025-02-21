from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Lista de inscritos (simples, sem banco de dados por enquanto)
inscritos = []

@app.route('/')
def index():
    return render_template('index.html', inscritos=inscritos, theme_colors=["#D8E2DC", "#FFE5D9", "#FFCAD4", "#F4ACB7", "#9D8189"])

@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.json.get('nome')
    if nome and nome not in inscritos:
        inscritos.append(nome)
    return jsonify(inscritos)

@app.route('/remover', methods=['POST'])
def remover():
    nome = request.json.get('nome')
    if nome in inscritos:
        inscritos.remove(nome)
    return jsonify(inscritos)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Obtém a porta do ambiente ou usa 5000
    app.run(host="0.0.0.0", port=port)


