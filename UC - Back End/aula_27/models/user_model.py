from database import get_connection

def create_user(nome,email,senha):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO users (nome,email,senha) VALUES (?,?,?)",(nome,email,senha))
    conn.commit()
    cursor.close()
    conn.close()
    
def get_user_by_email(email):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=?",(email,))
    email=cursor.fetchone()
    cursor.close()
    conn.close()
    return email

def get_user_by_id(user_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id=?",(user_id,))
    user=cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def update_user(user_id,nome,email):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("UPDATE users SET nome=?,email=? WHERE id=?",(nome,email,user_id))
    conn.commit()
    cursor.close()
    conn.close()