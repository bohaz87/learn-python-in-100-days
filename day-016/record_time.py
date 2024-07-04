import time
import random

def record_time(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print(f'{func.__name__} spent time: {end - start:.3f}s')
		return result
	return wrapper

download = record_time(lambda: time.sleep(random.randint(2, 4)))
download()

upload = record_time(lambda: time.sleep(random.randint(1, 3)))
upload()

@record_time
def sleep(n:int):
	time.sleep(random.randint(0, n))

sleep(1)