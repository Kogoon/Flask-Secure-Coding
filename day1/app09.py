from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    name = '홍길동'
    home = 'Seoul'
    if request.args.get('name'):
        name = request.args['name']
    if request.args.get('home'):
        home = request.args['home']

    return render_template(
            'app09.html', name=name, home=home)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

