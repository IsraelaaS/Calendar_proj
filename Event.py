from datetime import timedelta, datetime
class Event:
    
    def __str__(self):
        return f'\nEvent: {self.name}\nStart Time: {self.start_t}\nEnd Time: {self.end_t}\nDescription: {self.description}'

    # Method to be used for deleting events from list in main file
    def __eq__(self, other):
        return self.name==other.name and self.date==other.date and self.start_t==other.start_t and self.end_t==other.end_t
    
    # when dates are equal compare starting time
    def __lt__(self, other):
        if self.date != other.date:
            return self.date < other.date
        else:
            return self.start_t < other.start_t
            
    def __init__(self, name, date, start_t, end_t, descr):
        self.date=date
        self.name=name
        if len(descr) == 0:
            self.description = 'Empty'
        else:
            self.description=descr
        self.start_t= start_t
        self.end_t=end_t
        # self call to internalize each objec to have a string object