
from flask import Flask, jsonify, request, render_template
from requests import get
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info('app_info', 'Informações da Aplicação', version = '0.0.1')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/naruto')
def naruto():
    return jsonify(
        get('https://api.jikan.moe/v4/anime?q=Naruto&sfw').json()
    )

@app.route('/busca-cep', methods = ['GET'])
def cep():
    num_cep = request.args.get('cep')
    return jsonify(
        get(f'''https://viacep.com.br/ws/{num_cep}/json/''').json()
    )

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)
