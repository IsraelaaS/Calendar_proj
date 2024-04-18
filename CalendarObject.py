import tkinter as tk
import calendar_list_container

class CalendarObject:

    
    def __init__(self, CalendarLabel):


        # this list will hold the calendar_list_container
        # the calendar list container is a object that has a value and a list and the value is the day that it represents
        # the list is the events that have that day
        self.events = []
        self.root = CalendarLabel
       
        self.Previous_Button = tk.Button(self.root, text = '<', command = self.decrement_date_index)
        self.Previous_Button.config(font=("Helvetica", 16))
        self.Previous_Button.place(relx=0.0, rely=0.0, anchor='nw') # Top Left
        #self.Previous_Button.pack()

        self.label = tk.Label(self.root, text = '', bg = 'black', fg = 'white')
        self.label.config(font=("Helvetica", 16))
        self.label.place(relx=0.5, rely=0.0, anchor='n')  # Top center
        #self.label.pack()

        self.Next_Button = tk.Button(self.root, text = '>', command = self.increment_date_index)
        self.Next_Button.config(font=("Helvetica", 16))
        self.Next_Button.place(relx=1.0, rely=0.0, anchor='ne')  # Top right
        #self.Next_Button.pack()

        self.current_date_index = 0

    # used to increment date index to go forward by a date
    # checks for less than the length of the list to avoid out of bounds
    def increment_date_index(self):
        if self.current_date_index < len(self.events) - 1:
            self.current_date_index += 1
            self.refresh()

    # used to decrement date index to go back by a date
    # checks for greater than 0 to avoid out of bounds
    def decrement_date_index(self):
            if self.current_date_index > 0:
                self.current_date_index -= 1
                self.refresh()
                
    def add_event(self, event):

        # if there are no events in the list, add the event to the list and return
        if len(self.events) == 0:
            calendarObj = calendar_list_container.calendar_date_container(event.date, event)
            self.events.append(calendarObj)
            return
        
        # if the event is already in the list, add the event to the list and return
        for e in self.events:
            if event.date == e.date:
                e.add_event(event)
                return
        # creates a new calendar object and adds it to the list
        calendarObj = calendar_list_container.calendar_date_container(event.date, event)
        self.events.append(calendarObj)


    def __str__(self):
        return 'Current Date:'+ self.events[self.current_date_index].date + '\n' + 'Events:'+ str(self.events) + '\n'
    
    # refreshs text on label
    # uses current index as the event to show rather than showing all of them at once
    def refresh(self):
        self.label.config(text = str(self.events[self.current_date_index].date) + '\n' + 'Events:'+ str(self.events[self.current_date_index]))