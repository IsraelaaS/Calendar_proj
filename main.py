from Event import Event
import datetime

# list containing all events
Events=[]


#
def add_events():
    name= input("Enter name of event: ")
    date= input_date("Enter date of event (mm/dd/yyyy): ")
    start= input_time("Enter start time of event (HH:MM): ")
    end= input_time("Enter end time of even (HH:MM): ")

    # error check for start time being after end time
    while end <= start:
        print("End time must be after start time.")
        end= input_time("Enter end time of event (HH:MM): ")
    description=""
    des_yn = input("Do you want to add a description? Y or N ")
    if des_yn == "Y":
        description = input("Enter the description: ")
    else:
        description = "None"
    
    new_Event= Event(name, date, start, end, description)

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

def main():
    add_events()
    list_all()

if __name__ == "__main__":
    main()