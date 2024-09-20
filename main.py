from flask import Flask, request, jsonify, abort

app = Flask(__name__)

@app.route('/status/<int:code>', methods=['GET'])
def return_status_code(code):
    # Verificar si es un código HTTP válido
    if 100 <= code <= 599:
        return jsonify({"message": f"Returning status code {code}"}), code
    else:
        abort(400, description="Invalid HTTP status code")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
