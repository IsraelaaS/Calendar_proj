from Event import Event
from datetime import timedelta, datetime
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
        return name_str.get()
    else:
        # prompt reentry of field
        name_warning_label.config(text = 'Name Field Cannot Be Empty')
        name_str.set('')
        return False
    
# Carter
# user input string checked against proper date format
def validate_date_entry(date_str, date_warning_label):
    try:
        date_warning_label.config(text = '')
        date_time = datetime.strptime(date_str.get(), '%m/%d/%Y')
        return date_time.date()
    except ValueError:
        date_warning_label.config(text = 'Invalid Date Format. Please Enter A Time In The Correct Format')
        date_str.set('')
        return False
    
# Carter
# Input time prompt
# loops to retrieve user input in correct xx:xx format
# returns formatted time
def validate_time_entry(time_str, time_warning_label):
        try:
            time_warning_label.config(text = '')
            return datetime.strptime(time_str.get(), '%H:%M').time()
        except ValueError:
            time_warning_label.config(text = 'Invalid Date Format')
            time_str.set('')
            return False
        
def compare_time(start_time, end_time, time_warning_label):
    if start_time < end_time:
        return True
    time_warning_label.config(text = 'Start Time Must Be Before End Time')
    return False

# check all fields are complete
# once done set to destroy
def submit_form(name_string, name_entry_field, name_warning_label, name_label,
                date_string, date_entry_field, date_warning_label, date_label,
                start_time_string, start_time_entry_field, start_time_warning_label, start_time_label,
                end_time_string, end_time_entry_field, end_time_warning_label, end_time_label,
                description_string, description_entry_field, description_label,
                textbox,
                submit_button,
                add_event_button):
    
    # getting boolean 
    valid_name = validate_name_entry(name_string, name_warning_label)
    valid_date = validate_date_entry(date_string, date_warning_label)
    
    valid_start_time = validate_time_entry(start_time_string, start_time_warning_label)
    valid_end_time = validate_time_entry(end_time_string, end_time_warning_label)


    start_end_time_order = compare_time(valid_start_time, valid_end_time, start_time_warning_label)

    

    # all fields completed properly to be destroyed
    if valid_name and valid_date and valid_start_time and valid_end_time and start_end_time_order:

        name_entry_field.destroy()
        name_label.destroy()
        name_warning_label.destroy()

        date_entry_field.destroy()
        date_label.destroy()
        date_warning_label.destroy()

        start_time_entry_field.destroy()
        start_time_label.destroy()
        start_time_warning_label.destroy()

        end_time_entry_field.destroy()
        end_time_label.destroy()
        end_time_warning_label.destroy()

        description_entry_field.destroy()
        description_label.destroy()

        submit_button.destroy()

        # create event object, add to list and refresh text box
        current_event = Event(valid_name, valid_date, valid_start_time, valid_end_time, description_string.get())
        Events.append(current_event)
        Events.sort(reverse = True)
        event_refresh_text(textbox)
        # reenables button once submit is fully submited
        add_event_button['state'] = 'normal'
        
# puts everything on label to ask for input
# requires textbox to be able to refresh when form is submitted
def gui_add_events(label, textbox, add_event_button):


    # name label field
    name_label = tk.Label(label, text = 'Name', bg = 'lightblue')
    name_label.pack()
    name_string = tk.StringVar()
    name_entry_field = tk.Entry(label, textvariable = name_string)
    name_entry_field.pack()

    #name warning label
    name_warning_label = tk.Label(label, text = '', fg = 'red', bg = 'lightblue')                       
    name_warning_label.pack()


    # date label field
    date_label = tk.Label(label, text = 'Date: mm/dd/yyyy', bg = 'lightblue')
    date_label.pack()
    date_string = tk.StringVar()
    date_entry_field = tk.Entry(label, textvariable = date_string)
    date_entry_field.pack()

    # date warning label
    date_warning_label = tk.Label(label, text = '', fg = 'red', bg = 'lightblue')
    date_warning_label.pack()


    # start time label
    start_time_label = tk.Label(label, text = 'Start Time HH:MM', bg = 'lightblue')
    start_time_label.pack()
    start_time_string = tk.StringVar()
    start_time_entry_field = tk.Entry(label, textvariable= start_time_string)
    start_time_entry_field.pack()

    start_time_warning_label = tk.Label(label, text = '', fg = 'red', bg = 'lightblue')
    start_time_warning_label.pack()

    # start time label
    end_time_label = tk.Label(label, text = 'End Time HH:MM', bg = 'lightblue')
    end_time_label.pack()
    end_time_string = tk.StringVar()
    end_time_entry_field = tk.Entry(label, textvariable= end_time_string)
    end_time_entry_field.pack()

    end_time_warning_label = tk.Label(label, text = '', fg = 'red', bg = 'lightblue')
    end_time_warning_label.pack()

    description_label = tk.Label(label, text = 'Optional Description', bg = 'lightblue')
    description_label.pack()
    description_string = tk.StringVar()
    description_entry_field = tk.Entry(label, textvariable= description_string)
    description_entry_field.pack()


    submit_button = tk.Button(label, text = 'Submit', 
                              # sends all strings and labels, forms to be checked and if checked then destroyed
                              command = lambda: submit_form(
                                                            name_string, name_entry_field, name_warning_label, name_label,
                                                            date_string, date_entry_field, date_warning_label, date_label,
                                                            start_time_string, start_time_entry_field, start_time_warning_label, start_time_label,
                                                            end_time_string, end_time_entry_field, end_time_warning_label, end_time_label,
                                                            description_string, description_entry_field, description_label,
                                                            textbox,
                                                            submit_button,
                                                            add_event_button
                                                            ))
    submit_button.pack()

def event_refresh_text(textbox):
    # clears listbox
    textbox.delete('1.0', tk.END)

    # check for empty array
    if len(Events) == 0:
        textbox.insert(tk.END, 'Event list is empty')
    else:
        for i, e in enumerate(Events):
            textbox.insert(tk.END, str(e))
            if i != len(Events) - 1: # when an item has another item next it will add a break inbetween
                textbox.insert(tk.END, '\n\n------------------\n')



def main():
    # main while loop to reprompt for user input
    # Carter

    #Setting up main frame
    root_GUI = tk.Tk()
    root_GUI.title("Calendar")
    root_GUI.geometry("1200x800")

    # primary background that everything is set on
    main_frame = tk.Frame(root_GUI, bg = 'black')
    main_frame.pack(fill = 'both', expand = True)

     # Two column layout
    main_frame.columnconfigure(0, weight=1)  # For the left portion
    main_frame.columnconfigure(1, weight=1)  # For the right portion
    main_frame.rowconfigure(0, weight=1)

    event_text_frame = tk.LabelFrame(main_frame, bg = 'black', fg = 'white', highlightthickness = 0, font = ("Arial", 12))
    event_text_frame.grid(row = 0, column = 0, padx = 10, pady = 10, sticky='nsew')

    labels = []
    for i in range(7):
        label = tk.Label(event_text_frame, text=str(datetime.now().date() + timedelta(days=i)), width=10, height=2)
        label.grid(row=0, column=i)
        labels.append(label)

    
    
    buttons_frame = tk.LabelFrame(main_frame, text = "Options", bg = 'lightblue')
    buttons_frame.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = 'nsew')

    refresh_events_button = tk.Button(buttons_frame, text = 'Refresh Events', command = lambda: event_refresh_text(event_text_frame))
    refresh_events_button.pack()

    # called through the button only to reenable the button once adding to events is finished
    def add_event_and_enable_button():
        gui_add_events(buttons_frame, event_text_frame, add_event_button) 
    
    add_event_button = tk.Button(buttons_frame, text = 'Add Event', command = lambda: [add_event_button.config(state = 'disabled'), add_event_and_enable_button()])
    add_event_button.pack()

    root_GUI.mainloop()


if __name__ == "__main__":
    main()
