from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    name = request.args.get('name')
    name = replace_special_character(name)
    return '<h1>HEllo, %s!</h1>'%(name)


def replace_special_character(val):
    val = val.replace('&', '&amp;')
    val = val.replace('<', '&lt;')
    val = val.replace('>', '&gt;')
    val = val.replace('"', '&quot;')
    val = val.replace("'", '&#x27;')
    val = val.replace('/', '&#x2f;')
    val = val.replace('(', '&#x40;')
    val = val.replace(')', '&#x41;')
    return val


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
