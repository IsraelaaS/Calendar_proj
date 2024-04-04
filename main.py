from Event import Event
import datetime
import tkinter as tk

# list containing all events
Events = []


# Searches through events
def list_all():
    if len(Events) == 0:
        print("No events")
    else:
        for event in Events:
            event.__str__()
            print("\n********************")


def list_events_day():
    print("List of events")


# Carter
# Input time prompt
# loops to retrieve user input in correct xx:xx format
# returns formatted time
def input_time(prompt):
    while True:
        time_str = input(prompt)
        try:
            return datetime.datetime.strptime(time_str, '%H:%M').time()
        except ValueError:
            print("Invalid time format. Please enter a time in the format 'HH:MM'")


# Israel
# Used to delete events from Event list; should only delete first match
def delete_event(f_event):
    for event in Events:
        if f_event == event.name:
            Events.remove(event)
            return print(f_event + " has been deleted\n")


# Israel
# Method to check duplicate events within Event list
def check_dup(f_event):
    for event in Events:
        if f_event.__eq__(event):
            print(f_event.name + " is already registered")
            return True
    return False


# Israel event editor function
def edit_event(f_event):
    for event in Events:
        if f_event == event.name:
            c_name = input("Do you want to change name? Y or N")
            if c_name == "Y":
                event.name = input("Enter new event name: ")
            c_date = input("Do you want to change date? Y or N")
            if c_date == "Y":
                event.date = input("Enter new event date: ")
            c_start_time = input("Do you want to change start time? Y or N")
            if c_start_time == "Y":
                event.start_t = input("Enter new event start time: ")
            c_end_time = input("Do you want to change end time? Y or N")
            if c_end_time == "Y":
                event.end_t = input("Enter new event end time: ")
            c_description = input("Do you want to change description? Y or N")
            if c_description == "Y":
                event.description = input("Enter new event description: ")
            return print("Changed event name: " + event.name)
        else:
            print("Event not found")

# Carter
# takes string and label to write when form is not properly filled
def validate_name_entry(name_str, name_warning_label):
    # validating name field to not be empty
    if name_str.get() != '':
        name_warning_label.config(text = '')
        # set to be destroyed
        return True
    else:
        # prompt reentry of field
        name_warning_label.config(text = 'Name Field Cannot Be Empty')
        name_str.set('')
        return False
    
# Carter
# user input string checked against proper date format
def validate_date_entry(date_str, date_warning_label):
    try:
        datetime.datetime.strptime(date_str.get(), '%m/%d/%Y')
        date_warning_label.config(text = '')
        return True
    except ValueError:
        date_warning_label.config(text = 'Invalid Date Format. Please Enter A Time In The Correct Format')
        date_str.set('')
        return False

# check all fields are complete
# once done set to destroy
def submit_form(name_string, name_entry_field, name_warning_label, name_label,
                date_string, date_entry_field, date_warning_label, date_label,
                submit_button):
    
    # getting boolean 
    valid_name = validate_name_entry(name_string, name_warning_label)
    valid_date = validate_date_entry(date_string, date_warning_label)

    # all fields completed properly to be destroyed
    if valid_name and valid_date:

        name_entry_field.destroy()
        name_label.destroy()
        name_warning_label.destroy()

        date_entry_field.destroy()
        date_label.destroy()
        date_warning_label.destroy()

        submit_button.destroy()
        

def gui_add_events(label):


    # name label field
    name_label = tk.Label(label, text = 'Name')
    name_label.pack()
    name_string = tk.StringVar()
    name_entry_field = tk.Entry(label, textvariable = name_string)
    name_entry_field.pack()

    name_warning_label = tk.Label(label, text = '', fg = 'red')
    name_warning_label.pack()


    # date label field
    date_label = tk.Label(label, text = 'Date: mm/dd/yyyy')
    date_label.pack()
    date_string = tk.StringVar()
    date_entry_field = tk.Entry(label, textvariable = date_string)
    date_entry_field.pack()

    date_warning_label = tk.Label(label, text = '', fg = 'red')
    date_warning_label.pack()

    submit_button = tk.Button(label, text = 'Submit', 
                              # sends all strings and labels, forms to be checked and if checked then destroyed
                              command = lambda: submit_form(name_string, name_entry_field, name_warning_label, name_label,
                                                            date_string, date_entry_field, date_warning_label, date_label,
                                                            submit_button))
    submit_button.pack()


def main():
    # main while loop to reprompt for user input
    # Carter

    #Setting up main frame
    root_GUI = tk.Tk()
    root_GUI.title("Calendar")
    root_GUI.geometry("1200x800")

    # Two column layout
    root_GUI.columnconfigure(0, weight=1)  # For the left portion
    root_GUI.columnconfigure(1, weight=1)  # For the right portion
    root_GUI.rowconfigure(0, weight=1)

    buttons_frame = tk.LabelFrame(root_GUI, text = "Options", bg = 'lightblue')
    buttons_frame.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = 'nsew')
    

    button = tk.Button(buttons_frame, text = 'Add Event', command = lambda: gui_add_events(buttons_frame))
    button.pack()


    root_GUI.mainloop()


if __name__ == "__main__":
    main()
