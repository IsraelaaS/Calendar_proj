class calendar_date_container:
    def __init__(self, date_int, event):

        self.events = []
        self.date_int = date_int
        self.events.append(event)

    
    def __eq__ (self, other):
        return self.date_int == other.date_int
    
    def __lt__ (self, other):
        return self.date_int < other.date_int
    
    def add_event(self,event):
        self.events.append(event)

    def __str__(self):
        return f'\n===========\nDate: {self.date_int}, Events: {", ".join(str(e) for e in self.events)}'