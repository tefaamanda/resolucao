from flask import Flask, render_template, request, redirect
app = Flask(__name__)

contatos = []


@app.route('/')
def index():
    return render_template('calculadoram.html', contatos=contatos)


@app.route('/adicionar_contato', methods=['GET', 'POST'])
def adicionar_contato():
    """
    Rota para adicionar um novo contato.
    Se o método for POST, adiciona o novo contato à lista.
    Se não, exibe o formulário para adicionar um novo contato.
    """
    if request.method == 'POST':
        nomeanimal = request.form['nome']
        especie = request.form['especie']
        raca = request.form['raca']
        peso = request.form['peso']
        nometutor = request.form['nometutor']
        telefone = request.form['telefone']
        codigo = len(contatos)
        contatos.append([codigo, nomeanimal, especie, raca, peso, nometutor, telefone])
        return redirect('/')  # Redireciona de volta para a página inicial
    else:
        return render_template('adicionar_contato.html')  # Renderiza o formulário de adicionar contato


@app.route('/editar_contato/<int:codigo>', methods=['GET', 'POST'])
def editar_contato(codigo):
    """
    Rota para editar um contato existente.
    Se o método for POST, atualiza os detalhes do contato com o ID fornecido.
    Caso contrário, exibe o formulário preenchido com os detalhes do contato para edição.
    """
    if request.method == 'POST':
        nomeanimal = request.form['nome']
        especie = request.form['especie']
        raca = request.form['raca']
        peso = request.form['peso']
        nometutor = request.form['nometutor']
        telefone = request.form['telefone']
        contatos[codigo] = [codigo, nomeanimal, especie, raca, peso, nometutor, telefone]
        return redirect('/')  # Redireciona de volta para a página inicial
    else:
        contato = contatos[codigo]
        return render_template('editar_contato.html', contato=contato)  # Renderiza o formulário de edição


@app.route('/apagar_contato/<int:codigo>')
def apagar_contato(codigo):
    """
    Rota para apagar um contato da lista.
    """
    del contatos[codigo]
    return redirect('/')  # Redireciona de volta para a página inicial

@app.route('/calculadoram')
def calculadoram():
    return render_template('calculadoram.html', resultado='')

@app.route('/resultado', methods=['POST'])
def resultado():
    pesoanimal = float(request.form['peso'])
    graudesidrata = request.form['desidratação']

    if pesoanimal > 0:
        if graudesidrata.upper() == 'LEVE':
            soroml = pesoanimal * 50
            quantidade = f'Você deve aplicar {soroml}ml de soro '
        elif graudesidrata.upper() == 'MODERADA':
            soroml = pesoanimal * 75
            quantidade = f'Você deve aplicar {soroml}ml de soro '
        elif graudesidrata.upper() == 'GRAVE':
            soroml = pesoanimal * 100
            quantidade = f'Você deve aplicar {soroml}ml de soro '
        else:
            quantidade = 'Isso não é um grau válido'

    else:
        quantidade = f'Isso não é um peso válido'

    return render_template('calculadoram.html', resultado=f'{quantidade}')


if __name__ == '__main__':
    app.run(debug=True)