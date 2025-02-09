'''learn how to read a file in python and begin outlining the porject'''
'''look at the graphic of all the elements necessary for the project'''
'''read from file to get blood and write back with updated blood sugar levels'''
'''whenever there is an update in the blood sugar write to a file with the date and time and the amount of insulin'''
'''read textbook for examples or sanarios and see how timing plays into dose amount'''
'''we also need to gather statistics about the person, those can either be entered by us or put in the text file'''
import time
# mathmatical calculation to be called by test_blood() --> Will H
def blood_sugar_calc() :

# read data from body.txt which simulates blood from consumer --> Nick 
def read_blood(): 

# interpret data from read_blood() and pass it to dispense_insulin()
def test_blood():

# store change make to the blood stream in updated_blood.txt --> Joe
def store_result(insulin_type, units):
    file = open("Results", "a")
    current_time = time.ctime()
    file.write('Date/Time of dose: ' + current_time + ', Units dispensed: ' + units + ', Type: ' + insulin_type + '\n')
    file.close()
store_result('basal', '10')
# dispense insulin based on results from test_blood() --> Will L
def dispense_insulin():

# individuals 'account' --> name, birthday, weight, etc.
def persons_attributes():



