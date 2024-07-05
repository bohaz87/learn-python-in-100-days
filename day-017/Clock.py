import time

class Clock:
	def __init__(self, hour = 0, minute=0, second=0) -> None:
		self.hour = hour
		self.minute = minute
		self.second = second

	def run(self):
		self.second += 1
		if (self.second == 60):
			self.second = 0
			self.minute += 1
			if (self.minute == 60):
				self.minute = 0
				self.hour += 1
				if (self.hour == 24):
					self.hour = 0
	
	def show(self):
		return f'{self.hour:0>2d}:{self.minute:0>2d}:{self.second:0>2d}'

clock = Clock(23, 59, 58)
while True:
	print(clock.show())
	time.sleep(1)
	clock.run()
