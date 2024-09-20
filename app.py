from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Ruta principal que describe cómo utilizar la app
@app.route('/')
def index():
    return jsonify({
        "message": "Bienvenido a HTTP Status Code Emulator!",
        "usage": "Para usar este servicio, enviar un request GET a '/status/<code>',  donde <code> es un codigo HTTP válido. (e.j., /status/200, /status/404)."
    })

# Ruta que devuelve el código HTTP solicitado
@app.route('/status/<int:code>', methods=['GET'])
def return_status_code(code):
    # Verificar si es un código HTTP válido
    if 100 <= code <= 599:
        return jsonify({"message": f"Returning status code {code}"}), code
    else:
        abort(400, description="Invalid HTTP status code")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
