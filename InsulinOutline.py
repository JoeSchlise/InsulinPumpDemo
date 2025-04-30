'''learn how to read a file in python and begin outlining the porject'''
'''look at the graphic of all the elements necessary for the project'''
'''read from file to get blood and write back with updated blood sugar levels'''
'''whenever there is an update in the blood sugar write to a file with the date and time and the amount of insulin'''
'''read textbook for examples or sanarios and see how timing plays into dose amount'''
'''we also need to gather statistics about the person, those can either be entered by us or put in the text file'''
import time
import random
import customtkinter
import threading
from PIL import Image
from web import file


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
def store_result(insulin_type, units, blood, new_blood, filepath):
    print(filepath + "this is the file from web")
    file2 = open(filepath, "a")
    current_time = time.ctime()
    file2.write(
        f"{current_time:<25} "
        f"Blood: {blood:<5} "
        f"Units: {units:<3} "
        f"Type: {insulin_type:<6} "
        f"New Blood: {new_blood:<5}\n"
    )
    file2.close()
'''
#Function to call when changing the frame
def trigger_emergency():
    for widget in app.winfo_children():
        widget.destroy()  # Remove all existing UI elements

    app.configure(bg="red")  # Change background to red

    alert_label = customtkinter.CTkLabel(
        app, text="CALL 911!", font=("Arial", 48, "bold"), text_color="white", width=600, height=300
    )
    alert_label.pack(expand=True)  # Center the label

    stop_button = customtkinter.CTkButton(
        app, text="Acknowledge", font=("Arial", 24), command=reset_ui
    )
    stop_button.pack(pady=20)

def reset_ui():
    for widget in app.winfo_children():
        widget.destroy()  # Clear emergency screen
    app.configure(bg="SystemButtonFace")  # Reset background
    tab1()  # Restore main UI
# dispense insulin based on results from test_blood() --> Will L
'''
def dispense_insulin(count, file):

    units = 0
    new_blood = 0
    blood_sugar = int(read_blood())

    if blood_sugar >= 450 or blood_sugar < 70:
        with open("emergency.txt", "w") as f:
            f.write("true")
        return  # Stop insulin logic if emergency triggered

        # Clear emergency flag if levels are normal again
    with open("emergency.txt", "w") as f:
        f.write("false")

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

            return
        new_blood = blood_sugar - (units * 30)
    blood_sugar_file = open('body.txt', 'w')
    blood_sugar_file.write(str(new_blood))
    blood_sugar_file.close()
    store_result(name, str(units), str(blood_sugar), str(new_blood), file)



# individuals 'account' --> name, birthday, weight, etc.
def persons_attributes():
    F_name = input("Enter your first name: ")
    L_name = input("Enter your last name: ")
    b_day = input("Enter your Birthdate: ")
    weight = input("Enter weight: ")

THREAD_ON = True
def pump_running(file):
    try:

        print(THREAD_ON)
        count = 0
        while THREAD_ON:
            print("running")
            blood_randomizer()
            read_blood()
            time.sleep(5)
            dispense_insulin(count, file)
            count = count + 1
    except:
        print('SYSTEM NEEDS MAINTENANCE!!!!!')

def start_thread(file):
    global THREAD_ON
    THREAD_ON = True
    thread = threading.Thread(target=pump_running, args=(file,))
    thread.start()

def stop_pump():
    global THREAD_ON
    THREAD_ON = False
    print("Pump is turning off...")

'''

#This is UI setup/initialization
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.geometry("900x700")
app.title("Insulin Pump Software")


# This creates tabs that you can go back and forth on
def tab1():
    def tab2():
        title1.destroy()
        start_pump.destroy()
        view_result.destroy()
        stop.destroy()
        title2 = customtkinter.CTkLabel(app, font=("Arial", 24), width=400, height=100, text="Insulin Dispensing History")
        title2.pack(padx=10, pady=10)

        scrollable_frame = customtkinter.CTkScrollableFrame(app, width=500, height=250)
        scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # View data inside Scrollable Frame
        result = open('Results', 'r')
        data = result.read()
        result.close()

        text_widget = customtkinter.CTkLabel(scrollable_frame, text=data, font=("Arial", 14), width=600, height=230)
        text_widget.pack(padx=10, pady=10)
        def back():
            for widget in app.winfo_children():
                widget.destroy()
            tab1()
        back = customtkinter.CTkButton(app, font=("Arial", 20), width=400, height=100, text="Go Back", command=back)
        back.pack(pady=100)

    title1 = customtkinter.CTkLabel(app, font=("Arial", 24), width=400, height=100, text="Insulin Pump Commands")
    title1.pack(padx=10,pady=10)

    start_pump = customtkinter.CTkButton(app, font=("Arial", 20), width=350, height=100, text="Start Pump", command=start)
    start_pump.pack(padx=10, pady=10)

    view_result = customtkinter.CTkButton(app, font=("Arial", 20), width=350, height=100, text="View Result", command=tab2)
    view_result.pack(padx=10, pady=10)

    stop = customtkinter.CTkButton(app, font=("Arial", 20), width=350, height=100, text="Stop Pump", command=stop_pump)
    stop.pack(padx=10, pady=10)

tab1()

#Run app
app.mainloop()

'''
