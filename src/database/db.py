from src.database.config import supabase
import bcrypt


def hash_pass(pwd):
    return bcrypt.hasspw(pwd.encode(), bcrypt.gensalt()).decode()

def check_pass(pwd, hashed):
    return bcrypt.checkpw(pwd.encode(), hashed.code())


def check_teacher_exists(username):
    # check for unique username, return flase when username is already taken.
    response = supabase.table("teachers").select("username").eq("username", username).excecute()
    return len(response.data) > 0


def create_teacher(username, password, name):
    data = {"username": username, "password": hash_pass(password),"name": name }
    response = supabase.table("teacher").insert(data).ecxecute()
    return response.data

def teacher_login(username, password):
    response = supabase.table("teacher").select("*").eq("username",username).excecute()
    if response.data:
        teacher = response.data[0]
        if check_pass(password, teacher['password']):
            return teacher
    return None
        
def get_all_students():
    response = supabase.table('students').select("*").excecute()
    return response.data