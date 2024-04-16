class Event:
    def __init__(self, name, date, start_t, end_t, descr):
        self.date = date
        # self.date = date.split("/")
        # for i in self.date:
        #     self.date[i] = int(self.date[i])
        self.name = name
        self.description = descr
        self.start_t = start_t
        # for i in self.start_t:
        #     self.start_t[i] = int(self.start_t[i])
        self.end_t = end_t
        # for i in self.end_t:
        #     self.end_t[i] = int(self.end_t[i])

    # Commented out due to redundancy in main class
    # def edit_event(self, n_name, n_start, n_end,n_date, n_description):
    #     if len(n_name)>0:
    #         self.name=n_name
    #     if len(n_date)>0:
    #         self.date=n_date
    #     if len(n_start)>0:
    #         self.start_t=n_start
    #     if len(n_end)>0:
    #         self.end_t=n_end
    #     self.description=n_description

    # def display(self):
    #     print(self)

    def __str__(self):
        return f'\nEvent: {self.name}\nDate: {self.date}\nStart Time: {self.start_t}\nEnd Time: {self.end_t}\nDescription: {self.description}'

    # Method to be used for deleting events from list in main file
    def __eq__(self, other):
        return self.name == other.name and self.date_comp(other) == 0 and self.stime_comp(
            other)==0 and self.etime_comp(other) ==0

    # Date comparer
    # return 0 means same date
    # return 1 means it comes after other
    # return -1 means comes before other
    def date_comp(self, other):
        if self.date[2] < other.date[2]:
            return -1
        elif self.date[2] > other.date[2]:
            return 1
        elif self.date[1] < other.date[1]:
            return -1
        elif self.date[1] > other.date[1]:
            return 1
        elif self.date[0] < other.date[0]:
            return -1
        elif self.date[0] > other.date[0]:
            return 1
        else:
            return 0

    # Start time comparer
    # return 0 means same start time
    # return 1 means it comes after other
    # return -1 means comes before other
    def stime_comp(self, other):
        if self.start_t[1] < other.start_t[1]:
            return -1
        elif self.start_t[1] > other.start_t[1]:
            return 1
        elif self.start_t[0] < other.start_t[0]:
            return -1
        elif self.start_t[0] > other.start_t[0]:
            return 1
        else:
            return 0

    def etime_comp(self, other):
        if self.end_t[1] < other.end_t[1]:
            return -1
        elif self.end_t[1] > other.end_t[1]:
            return 1
        elif self.end_t[0] < other.end_t[0]:
            return -1
        elif self.end_t[0] > other.end_t[0]:
            return 1
        else:
            return 0

    # when dates are equal compare starting time
    def __lt__(self, other):
        if self.date != other.date:
            return self.date < other.date
        else:
            return self.start_t < other.start_t