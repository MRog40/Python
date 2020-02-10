# Simple class to represent times
class Time:
    # dunder (double underscore) methods are fundamental operations or values
    # given to basically all objects in python

    # Objects creation
    def __init__(self, hr, mi=0):
        hour = int(hr)
        minute = int((hr - hour)*60)
        self.hour = hour
        self.minute = minute + mi

    # Object's string representation
    def __str__(self):
        if self.hour > 12:
            h = self.hour - 12
            ampm = 'PM'
        else:
            h = self.hour
            ampm = 'AM'
        return '{}:{:02d} {}'.format(h, self.minute, ampm)
    
    def __repr__(self):
        return str(self)

    # How objects are added
    def __add__(self, other):
        m = self.minute + other.minute
        if m > 60:
            m -= 60
            h = 1
        else:
            h = 0
        h += self.hour + other.hour
        m = int(m+0.5)
        return Time(h, m)

    # And subtracted
    def __sub__(self, other):
        m = self.minute - other.minute
        if m < 0:
            m += 60
            h = -1
        else:
            h = 0
        h += self.hour - other.hour
        m = int(m+0.5)
        return Time(h, m)

    # Methods now, this method returns the double of hours of the object
    @property
    def hours(self):
        return self.hour + self.minute/60

    # Returns what time to leave from the start time given the time on card
    def leave_at(self, time_left_num=36):
        return self + Time(44) - Time(time_left_num)
