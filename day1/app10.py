import sqlite3

if __name__ == '__main__':
    
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    query = '''
        CREATE TABLE "tb_user" (
            "name" TEXT NOT NULL,
            "home" TEXT NOT NULL,
            PRIMARY KEY("name")
        );
    '''
    cursor.execute(query)

    query = 'INSERT INTO tb_user(name, home) VALUES(?, ?)'
    cursor.execute(query, ('shjeong', 'Seoul'))

    query = "SELECT * FROM tb_user"
    user_list = cursor.execute(query).fetchall()
    print(user_list)

    query = "UPDATE tb_user SET home=? WHERE name=?"
    cursor.execute(query, ('shjeong',))

    conn.commit()
    conn.close()
