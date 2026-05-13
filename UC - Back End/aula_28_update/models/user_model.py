from database import get_db_connection

def create_user(nome, email, senha):
    conn = get_db_connection()
    conn.execute('INSERT INTO users (nome, email, senha)VALUES(?,?,?)',
                 (nome, email, senha))
    conn.commit()
    conn.close()

def get_user_by_email(email):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
    conn.close()
    return user

def get_user_by_id(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    conn.close()
    return user

def update_user(user_id, nome, email):
    conn = get_db_connection()
    conn.execute('UPDATE users SET nome = ?, email = ? WHERE id = ?',
                 (nome, email, user_id))
    conn.commit()
    conn.close()
        