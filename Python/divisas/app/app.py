from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')

def index():

    data = {
        "mensaje": '!Mensaje de bienvenida!',
        "titulo": 'Un titulo'
    }

     
    return render_template('index.html',data=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)