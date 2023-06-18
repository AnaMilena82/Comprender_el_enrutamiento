from flask import Flask  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"


@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return 'Hola Mundo!'  # Localhost:5000/: haz que diga "¡Hola Mundo!"

@app.route('/dojo') #Localhost:5000/dojo: haz que diga "¡Dojo!"
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')# Crea un patrón y una función de URL que puedan manejar los siguientes ejemplos
def say(name):
    return "¡Hola, " + name
   


@app.route('/repeat/<int:num>/<string:cadena>') # Crea un patrón y una función de URL que puedan manejar los siguientes ejemplos (PISTA: int() puede ser útil Por ejemplo, int("35") devuelve 35):
def show_user_profile(num, cadena):
    result = ''
    for _ in range(num):
        result += cadena + "\n"
    return result


@app.route('/<path:path>') #Asegúrate de que si el usuario escribe cualquier ruta distinta a las especificadas, reciba un mensaje de error que diga "¡Lo siento! No hay respuesta. Inténtalo otra vez.”.
def error(path):
    return '¡Lo siento! No hay respuesta. Inténtalo otra vez.'

    






if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración

