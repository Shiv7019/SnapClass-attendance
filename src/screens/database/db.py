from src.screens.database.config import supabase

def check_teacher_exists(username):
    # ADDED .execute() at the end
    response = supabase.table('teachers').select('username').eq('username', username).execute()
    return len(response.data) > 0

def create_teacher(username, password, name):
    # ADDED .execute() at the end
    response = supabase.table('teachers').insert({
        "username": username,
        "password": password,
        "name": name
    }).execute()
    return response

def teacher_login(username, password):
<<<<<<< HEAD
    response = supabase.table('teachers').select('*').eq('username', username).eq('password', password).execute()
    print("DB RESULT:", response.data)          # ← debug
    if len(response.data) > 0:
        return response.data[0]
    return None
=======
    # ADDED .execute() at the end
    response = supabase.table('teachers').select('*').eq('username', username).eq('password', password).execute()
    return len(response.data) > 0
>>>>>>> origin/main
