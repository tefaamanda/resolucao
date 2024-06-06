from flask import Flask, render_template, request, redirect
app = Flask(__name__) #instacia flask no aplicativo

#lista
contatos = []

@app.route('/')
def index():
    return render_template('sumario.html', contatos=contatos)

@app.route('/agenda', methods=['GET', 'POST'])
def agenda():
    """
    Rota para agendar uma consulta.
    """
    if request.method == 'POST':
        nomea = request.form['nomea']
        nomet = request.form['nomet']
        data = request.form['data']
        sintomas = request.form['sintomas']
        codigo = len(contatos)
        contatos.append([codigo, nomea, nomet, data, sintomas])
        return redirect('/')  # Redireciona de volta para a página inicial
    else:
        return render_template('agenda.html')  # Renderiza o formulário de adicionar contato