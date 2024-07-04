import random
import time

def download(filename):
	print(f'start downloading {filename}')
	time.sleep(random.randint(2, 6))
	print(f'{filename} downloaded')

def upload(filename):
	print(f'start upload {filename}')
	time.sleep(random.randint(4, 8))
	print(f'{filename} uploaded')

start = time.time()
download('learn python.avi')
end = time.time()
print(f'spent time {end - start:.3f}s')

start = time.time()
upload('learn java.pdf')
end = time.time()
print(f'spent time {end - start:.3f}s')
	