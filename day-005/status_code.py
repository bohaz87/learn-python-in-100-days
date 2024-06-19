status_code = int(input('status code: '))
match status_code:
	case 400:
		description = 'Bad Request'
	case 401:
		description = 'Unauthorized'
	case 301 | 302:
		description = 'aaa'
	case _:
		description = 'unknown'

print('description: ', description)