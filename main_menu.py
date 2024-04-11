import tkinter as tk
from datetime import timedelta, datetime
from Event import Event

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
                calendar_visual,
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
        calendar_visual.add_event(current_event)
        calendar_visual.refresh()
        # reenables button once submit is fully submited
        add_event_button['state'] = 'normal'
        
# puts everything on label to ask for input
# requires textbox to be able to refresh when form is submitted
def gui_add_events(label, calendar_visual, add_event_button):

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
                                                            calendar_visual,
                                                            submit_button,
                                                            add_event_button
                                                            ))
    submit_button.pack()