from tinydb import TinyDB, Query

db = TinyDB('db_for_pump.json')

def create_account():
    name = input("Enter a Username: ")
    password = input("Enter a password: ")
    db.insert({'username': name, 'password': password, 'file_name' : name+password})


def error():
    print("Wrong credentials entered")

def login():
    name = input("Enter your username: ")
    password = input("Enter your password: ")

    table = db.table('_default')
    User = Query()

    user_temp = table.search(User.username == name)
    pass_temp = table.search(User.password == password)

    if user_temp == [] or pass_temp == []:
        error()
    else:
        print("Logging in")
        #set results file to be their results file



#create_account()
#login()
