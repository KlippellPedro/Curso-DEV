from database import get_connection

def create_user(nome,email,senha,foto):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (nome,email,senha,foto) VALUES (?,?,?,?)',(nome,email,senha,foto))
    conn.commit()
    cursor.close()
    conn.close()

def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def get_all_users():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM users')
    users=cursor.fetchall()
    cursor.close()
    conn.close()
    return users

def update_user(user_id, nome, email, senha, foto):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET nome = ?, email = ?, senha = ?, foto = ? WHERE id = ?', (nome, email, senha, foto, user_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    cursor.close()
    conn.close()