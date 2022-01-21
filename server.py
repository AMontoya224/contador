from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "estoessecreto"

contador = []

@app.route( '/', methods=['GET'] )
def paginaInicio():
    if session.get("contador") != None:
        contador.append(1)
    else:
        contador.clear()
    valor = len(contador)
    session["contador"] = valor
    return render_template( "index.html", valor=session["contador"])

@app.route( '/destroy_session', methods=["GET"] )
def resetearContador():
    session.clear()
    return redirect( '/' )

@app.route( '/two_visit', methods=['GET'] )
def paginaDosInicio():
    contador.append(1)
    return redirect( '/' )

# Para descodificar el coockie:
# import base64
# base64.urlsafe_b64decode('eyJjb250YWRvciI6OH0===')

@app.errorhandler(404)
def paginaNoEncontrada(error):
    return "¡Lo siento! No hay respuesta. Inténtalo mas tarde"

if __name__ == "__main__":
    app.run(debug=True)