from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Estilo do Rei Barbearia"

@app.route('/novofuncionario')
def adicionar_funcionario():
    return "funcionário adicionado"

@app.route('/novocliente')
def adiconar_cliente():
    return "Cliente cadastrado"
    
@app.route('/novoservico')
def adicionar_sevico():
    return "Serviço adicionado"

@app.route('/novoagendamento')
def agendamento_servico():
    return "Agendamento concluido"

@app.route('/login')
def tela_login():
    return "Tela Login"

@app.route('/logout')
def efetuar_logout():
    return "Logout efetuado"


app.run(debug=True)
