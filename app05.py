from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    name = request.args.get('name')
    return '<h1>Hello, %s!</h1>'%(name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)


