from database import get_db_connection

def create_user(nome, email, senha, is_admin=0):
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO users (nome, email, senha, is_admin)VALUES(?,?,?,?)',
        (nome,email,senha,is_admin)
    )
    conn.commit()
    conn.close()

def get_user_by_email(email): # buscar por email
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE email=?',(email,)).fetchone()
    conn.close()
    return user

def get_user_by_id(user_id): # buscar por id
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id=?',(user_id,)).fetchone()
    conn.close()
    return user    

def get_all_users(): # listar todos
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return users

def update_user(user_id, nome, email): # atualiza dados
    conn = get_db_connection()
    conn.execute('UPDATE users SET nome=?,email=? WHERE id=?',
                 (nome,email,user_id))
    conn.commit()
    conn.close()

def delete_user(user_id): # deletar dados
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE id=?',(user_id,))
    conn.commit()
    conn.close()    