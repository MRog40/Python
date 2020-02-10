# Simple class to represent times
class Time:
	# dunder (double underscore) methods are fundamental operations or values
	# given to basically all objects in python

	# Objects creation
	def __init__(self, hour, minute):
		self.hour = hour
		self.minute = minute

	# Object's string representation
	def __str__(self):
		if self.hour > 12:
			h = self.hour - 12
			ampm = 'PM'
		else:
			h = self.hour
			ampms = 'AM'
		return '{}:{:02d} {}'.format(h, self.minute, ampm)

	# How objects are added	
	def __add__(self, other):
		m = self.minute + other.minute
		if m > 60:
			m -= 60
			h = 1
		else: h = 0
		h += self.hour + other.hour
		m = int(m+0.5)
		return Time(h, m)
	
	# And subtracted
	def __sub__(self, other):
		m = self.minute - other.minute
		if m < 0:
			m += 60
			h = -1
		else: h = 0
		h += self.hour - other.hour
		m = int(m+0.5)
		return Time(h, m)

	# Another way to make an object from a double of hours
	@classmethod
	def from_num(cls, num):
		hour = int(num)
		minute = (num - hour)*60
		return cls(hour, minute)

	# Methods now, this method returns the double of hours of the object
	def raw_hours(self):
		return self.hour + self.minute/60
	
	# Returns what time to leave from the start time given the time on card
	def leave_at(self, time_left_num=32):
		return self + Time.from_num(40) - Time.from_num(time_left_num)

# When do I leave if I arrived at 7:28 and I already have 33.56 hours on my card
leave_time = Time(7, 28).leave_at(33.56)
print('\nLeave at {} for 40 hours.'.format(leave_time))

# How many hours will I have if I stay until 6 PM
total = Time(18, 0) - Time(7, 28) + Time.from_num(33.56)
print('You\'ll have {} hours if you leave at 6:00 PM.'.format(total.raw_hours()))