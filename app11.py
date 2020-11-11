from flask import Flask, request, render_template
import sqlite3


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    rows = []
    name = request.args.get('name')
    if name:
        conn = sqlite3.connect('app11.db')
        cursor = conn.cursor()
        query = "SELECT * FROM tb_user WHERE name='{}'".format(name)
        cursor.execute(query)
        rows = cursor.fetchall()
    else:
        name = 'Brown'

    return render_template('app11.html', rows=rows, name=name)


if __name__ == '__main__':
    conn = sqlite3.connect('app11.db')
    cursor = conn.cursor()

    query = '''
        CREATE TABLE IF NOT EXISTS "tb_user"(
            "name" TEXT NOT NULL,
            "home" TEXT NOT NULL,
            PRIMARY KEY("name")
            );
            '''
    cursor.execute(query)

    query = 'SELECT count(*) cnt FROM tb_user'
    rows = cursor.execute(query).fetchone()
    if rows[0] == 0:
        query = 'INSERT INTO tb_user(name, home) VALUES(?, ?)'
        cursor.execute(query, ('shjeong', 'Seoul'))
        cursor.execute(query, ('hong', 'Incheon'))
        cursor.execute(query, ('kim', 'Busan'))
        cursor.execute(query, ('park', 'Jeju'))
        conn.commit()
    
    conn.close()

    app.run(host='0.0.0.0')
