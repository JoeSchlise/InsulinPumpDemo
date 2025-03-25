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
    random_num = random.randint(30, 500)
    blood_sugar_file.write(str(random_num))
    blood_sugar_file.close()

# interpret data from read_blood() and pass it to dispense_insulin()


# store change make to the blood stream in updated_blood.txt --> Joe
def store_result(insulin_type, units, blood, new_blood):
    file = open("Results", "a")
    current_time = time.ctime()
    file.write('Date/Time of reading: ' + current_time + ', Blood reading: ' + blood + ', Units dispensed: ' + units + ', Type: ' + insulin_type +
               ', Read After Dose: ' + new_blood + '\n')
    file.close()


# dispense insulin based on results from test_blood() --> Will L
def dispense_insulin(count):
    units = 0
    new_blood = 0
    blood_sugar = int(read_blood())
    if count == 0: #first dose of the day
        name = "Basal"
        units = 10
        new_blood = 100
    else:
        name = "Bolus"
        if 200 <= blood_sugar <= 249:
            units = 2
        elif 250 <= blood_sugar <= 299:
            units = 4
        elif 300 <= blood_sugar <= 349:
            units = 6
        elif 350 <= blood_sugar <= 399:
            units = 8
        elif 400 <= blood_sugar <= 449:
            units = 10
        elif blood_sugar >= 450 or blood_sugar < 70:
            print("CALL 911")
        new_blood = blood_sugar - (units * 30)
    blood_sugar_file = open('body.txt', 'w')
    blood_sugar_file.write(str(new_blood))
    blood_sugar_file.close()
    store_result(name, str(units), str(blood_sugar), str(new_blood))



# individuals 'account' --> name, birthday, weight, etc.
def persons_attributes():
    F_name = input("Enter your first name: ")
    L_name = input("Enter your last name: ")
    b_day = input("Enter your Birthdate: ")
    weight = input("Enter weight: ")



#persons_attributes()
count = 0
for i in range(10):
    blood_randomizer()
    read_blood()
    time.sleep(5)
    dispense_insulin(count)
    count = count + 1
