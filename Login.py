from tinydb import TinyDB, Query

db = TinyDB('db_for_pump.json')

def create_account(new_username, new_password):
    db.insert({'username': new_username, 'password': new_password, 'file_name' : new_username+new_password + ".txt"})
    t_file = open(new_username+new_password + ".txt", "x")
    t_file.close()


def error():
    print("Wrong credentials entered")

def login(username, password):
    print("test")
    table = db.table('_default')
    User = Query()

    user = table.get((User.username == username) & (User.password == password))

    if user is None:
        error()
        return False, None
    else:
        print("Logged in as:", user['username'])
        print("User doc_id:", user.doc_id)  # Access the unique document ID
        return True, get_file(user.doc_id)

def get_file(id):
    table = db.table('_default')
    doc = table.get(doc_id=id)  # assuming user_id = 1
    if doc:
        file_name = doc['file_name']
        print("User's file name:", file_name)
        return file_name

#create_account()
#login()
