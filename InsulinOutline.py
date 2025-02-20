'''learn how to read a file in python and begin outlining the porject'''
'''look at the graphic of all the elements necessary for the project'''
'''read from file to get blood and write back with updated blood sugar levels'''
'''whenever there is an update in the blood sugar write to a file with the date and time and the amount of insulin'''
'''read textbook for examples or sanarios and see how timing plays into dose amount'''
'''we also need to gather statistics about the person, those can either be entered by us or put in the text file'''
import time
import random
# mathmatical calculation to be called by test_blood() --> Will H


# read data from body.txt which simulates blood from consumer --> Nick
def read_blood():
    blood_sugar_file = open('body.txt', 'r')
    blood_sugar = blood_sugar_file.read()
    blood_sugar_file.close()
    return blood_sugar

# populate the body.txt file with random data
def blood_randomizer():
    blood_sugar_file = open('body.txt', 'w')
    random_num = random.randint(70, 449)
    blood_sugar_file.write(str(random_num))
    blood_sugar_file.close()

# interpret data from read_blood() and pass it to dispense_insulin()


# store change make to the blood stream in updated_blood.txt --> Joe
def store_result(insulin_type, units):
    file = open("Results", "a")
    current_time = time.ctime()
    file.write('Date/Time of dose: ' + current_time + ', Units dispensed: ' + units + ', Type: ' + insulin_type + '\n')
    file.close()
store_result('basal', '10')

# dispense insulin based on results from test_blood() --> Will L
def dispense_insulin():
    units = 0
    if 200 <= int(read_blood()) <= 249:
        units = 2
    elif 250 <= int(read_blood()) <= 299:
        units = 4
    elif 300 <= int(read_blood()) <= 349:
        units = 6
    elif 350 <= int(read_blood()) <= 399:
        units = 8
    elif 400 <= int(read_blood()) <= 449:
        units = 10
    elif int(read_blood()) > 450:
        print("CALL 911")
    blood_sugar_file = open('body.txt', 'w')
    blood_sugar_file.write("100")
    blood_sugar_file.close()
    store_result('Bolus', str(units))



# individuals 'account' --> name, birthday, weight, etc.
def persons_attributes():
    F_name = input("Enter your first name: ")
    L_name = input("Enter your last name: ")
    b_day = input("Enter your Birthdate: ")
    weight = input("Enter weight: ")
    return F_name, L_name, b_day, weight


persons_attributes()
blood_randomizer()
read_blood()
time.sleep(5)
dispense_insulin()
