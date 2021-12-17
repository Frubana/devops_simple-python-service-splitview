from flask import Flask
app = Flask(__name__)

@app.route('/natgw-staticip-test/health-check')
@app.route('/health-check')
@app.route('/')
def hello_world():
    return 'Hello, MOoN! agregando tags \n nuevo servicio\n'

