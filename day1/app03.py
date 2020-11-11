from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return '<h1>Hello Flask!</h1>'

@app.route('/test', methods=['GET'])
def test():
    return '<h2>Testing</h2>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
