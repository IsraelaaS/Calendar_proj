import tkinter as tk
import calendar_list_container

class CalendarObject:

    
    def __init__(self, CalendarLabel):


        # this list will hold the calendar_list_container
        # the calendar list container is a object that has a value and a list and the value is the day that it represents
        # the list is the events that have that day
        self.events = []
        self.root = CalendarLabel
        
        
        
        
        
    def add_event(self, event):
        if len(self.events) == 0:
            calendarObj = calendar_list_container.calendar_date_container(event.date_int, event)
            self.events.append(calendarObj)
            return

        for e in self.events:
            if event.date_int == e.date_int:
                e.add_event(event)
                return
        
        calendarObj = calendar_list_container.calendar_date_container(event.date_int, event)
        self.events.append(calendarObj)

    def __str__(self):
        return '******\n'+ '\n'.join(str(date) for date in self.events)
    
    def refresh(self):
        templabel = tk.Label(self.root, text = )