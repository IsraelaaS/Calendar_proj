from Event import Event
import datetime

# list containing all events
Events=[]


def add_events():
    name= input("Enter name of event: ")
    date= input_date("Enter date of event (mm/dd/yyyy): ")
    start= input_time("Enter start time of event (HH:MM): ")
    end= input_time("Enter end time of even (HH:MM): ")

    # error check for start time being after end time
    while end <= start:
        print("End time must be after start time.")
        end= input_time("Enter end time of event (HH:MM): ")

    des_yn = input("Do you want to add a description? Y or N ")
    if des_yn == "Y":
        description = input("Enter the description: ")
    else:
        description = "None"
    
    new_Event= Event(name, date, start, end, description)

    # Israel
    # Check for duplicate events will be written here
    if check_dup(new_Event)==False:
        Events.append(new_Event)

def list_all():
    if len(Events)==0:
        print("No events")
    else:
        for event in Events:
            event.display()
def list_events_day():
    print("List of events")

# Carter 
# Input date prompt
# loops to retrieve user input in correct xx/xx/xxxx format
# returns formatted date
def input_date(prompt):
    while True:
        date_str = input(prompt)
        try:
            datetime.datetime.strptime(date_str, '%m/%d/%Y')
            return date_str
        except ValueError:
            print("Invalid date format. Please enter a date in the format 'mm/dd/yyyy'")

#Carter
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
        if f_event.__eq__(event):
            Events.remove(event)
            return print(f_event.name+" has been deleted")
    print()

# Israel
# Method to check duplicate events within Event list
def check_dup(f_event):
    for event in Events:
        if f_event.__eq__(event):
            print(f_event.name+" is already registered")
            return True
    return False


def main():
    # main while loop to reprompt for user input
    # Carter
    while True:
        print("What would you like to do")
        user_Answer = input("A Add Event | D Delete Event | L List All | E Exit\n")

        if user_Answer == 'A' or user_Answer == 'a':
            add_events()
        elif user_Answer == 'D' or  user_Answer == 'd':
            delete_answer = input("What is the name of the event you want to delete?")
            delete_event(delete_answer)
        elif user_Answer == 'L' or  user_Answer == 'l':
            list_all()
        elif user_Answer == 'E' or  user_Answer =='e':
            print("Exiting")
            break
        else:
            print("Invalid input try again")

        

if __name__ == "__main__":
    main()