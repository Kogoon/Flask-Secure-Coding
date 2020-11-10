from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = '홍길동' 
    home = 'Seoul'
    if request.method == 'POST':
        name = request.form['name']
        home = request.form['home']

    return render_template(
            'app08.html', name=name, home=home)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)


