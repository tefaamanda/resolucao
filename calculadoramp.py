from flask import Flask, render_template, request
app = Flask(__name__) #instacia flask no aplicativo

@app.route('/')
def index():
    return render_template('calculadoramp.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    dose = 0
    peso_animal = int(request.form['peso'])
    dose_rec = int(request.form['dose_r'])
    dose = peso_animal * dose_rec

    return render_template('calculadoramp.html', resultado=f"A dose a ser administrada ao animal é de {dose} mg/kg.")

if __name__ == '__main__':
    app.run(debug=True)