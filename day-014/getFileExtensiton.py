def get_file_extension(filename:str, ignore_dot=True):
	"""get file extension
	:param filename
	:param ignore_dot
	:return: file extension(suffix)
	"""
	pos = filename.rfind('.')
	if pos <= 0:
		return ''
	return filename[pos + 1:] if ignore_dot else filename[pos:]

print(get_file_extension('readme.txt'))
print(get_file_extension('readme.txt.md'))
print(get_file_extension('.readme'))
print(get_file_extension('readme.'))
print(get_file_extension('readme'))

from os.path import splitext

def get_file_extension2(filename: str, ignore_dot=True):
	ext = splitext(filename)[1][1:]
	return ext if ignore_dot or ext == '' else '.' + ext

print(get_file_extension2('readme.txt'))
print(get_file_extension2('readme.txt.md'))
print(get_file_extension2('.readme'))
print(get_file_extension2('readme.'))
print(get_file_extension2('readme'))
print('ignore dot = false'.center(30, '='))
print(get_file_extension2('readme.txt', False))
print(get_file_extension2('readme.txt.md', False))
print(get_file_extension2('.readme', False))
print(get_file_extension2('readme.', False))
print(get_file_extension2('readme', False))