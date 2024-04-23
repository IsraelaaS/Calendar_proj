class calendar_date_container:
    def __init__(self, date, event):

        self.events = []
        self.date = date

        # take date to int to store for sorting but
        # in all use cases of printing and showing to the user it should be in proper date format
        self.date_int = int(self.date.strftime("%m%d%Y"))
        self.events.append(event)

    def __eq__(self, other):
        return self.date_int == other.date_int

    def __lt__(self, other):
        return self.date_int < other.date_int

    def add_event(self, event):
        self.events.append(event)

    # Do not show date as it is handles in the parent class to string
    def __str__(self):
        return f'{", ".join(str(e) for e in self.events)}\n-----------'
