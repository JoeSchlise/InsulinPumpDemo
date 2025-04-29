from tinydb import TinyDB, Query

db = TinyDB('db_for_pump.json')

def create_account(new_username, new_password):
    db.insert({'username': new_username, 'password': new_password, 'file_name' : new_username+new_password})


def error():
    print("Wrong credentials entered")

def login(username, password):

    table = db.table('_default')
    User = Query()

    user_temp = table.search(User.username == username)
    pass_temp = table.search(User.password == password)

    if user_temp == [] or pass_temp == []:
        error()
        return False
    else:
        print("Logging in")
        return True
        #set results file to be their results file



#create_account()
#login()
