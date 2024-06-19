from flask import Flask, jsonify, request

app = Flask(__name__)

# Função para converter Celsius para Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Função para converter Celsius para Kelvin
def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

# Função para converter Dólar para Real
def usd_to_brl(usd):
    brl = usd * 5.5
    return brl

# Função para converter Euro para Real
def eur_to_brl(eur):
    brl = eur * 5.9
    return brl

# Rota para conversão de Celsius para Fahrenheit
@app.route('/celsius_to_fahrenheit', methods=['POST'])
def convert_celsius_to_fahrenheit():
    data = request.json
    celsius = data['celsius']
    fahrenheit = celsius_to_fahrenheit(celsius)
    return jsonify({'fahrenheit': fahrenheit})

# Rota para conversão de Celsius para Kelvin
@app.route('/celsius_to_kelvin', methods=['POST'])
def convert_celsius_to_kelvin():
    data = request.json
    celsius = data['celsius']
    kelvin = celsius_to_kelvin(celsius)
    return jsonify({'kelvin': kelvin})

# Rota para conversão de Dólar para Real
@app.route('/usd_to_brl', methods=['POST'])
def convert_usd_to_brl():
    data = request.json
    usd = data['usd']
    brl = usd_to_brl(usd)
    return jsonify({'brl': brl})

# Rota para conversão de Euro para Real
@app.route('/eur_to_brl', methods=['POST'])
def convert_eur_to_brl():
    data = request.json
    eur = data['eur']
    brl = eur_to_brl(eur)
    return jsonify({'brl': brl})

if __name__ == '__main__':
    app.run(debug=True)
