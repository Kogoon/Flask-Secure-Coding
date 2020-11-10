from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    name    = 'junsung'
    numbers = [1, 2, 3, 4, 5]
    flag    = True
    flag2   = False

    #{% %} - 반복(for), 분기(if)
    #{{ }} - 변수 값 표시
    #Template(jinja2) Client에게 노출이 되면 안되는 정보를 Server에서 표시하여 처리 
    return render_template(
            'app07.html', name=name, numbers=numbers, flag=flag, flag2=flag2)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
