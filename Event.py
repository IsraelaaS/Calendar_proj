class Event:
    def __init__(self, name, date, start_t, end_t, descr):
        self.date=date
        self.name=name
        self.description=descr
        self.start_t= start_t
        self.end_t=end_t


    def edit_event(self, n_name, n_start, n_end,n_date, n_description):
        if len(n_name)>0:
            self.name=n_name
        if len(n_date)>0:
            self.date=n_date
        if len(n_start)>0:
            self.start_t=n_start
        if len(n_end)>0:
            self.end_t=n_end
        self.description=n_description

    def display(self):
        print(self)

    def __str__(self):
        return f'Event: {self.name}\nDate: {self.date}\nStart Time: {self.start_t}\nEnd Time: {self.end_t}\nDescription: {self.description}'

