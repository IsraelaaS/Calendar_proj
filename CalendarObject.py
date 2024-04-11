import tkinter as tk

class CalendarObject:

    
    def __init__(self, CalendarLabel):

        self.events = []
        self.root = CalendarLabel
        
        
        self.selected_date = None
        self.year = 2024
        self.month = 4
        self.week = 1
        
        self.calendar = tk.Frame(self.root)
        self.calendar.pack(padx=10, pady=10)
        
        
    def add_event(self, event):
        date_int = event.date_int
        if self.events[date_int] == 0:
            # creates new list of objects
            self.events[date_int] = []
        
        self.events[date_int].append(event)