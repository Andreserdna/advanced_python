# def uppercase(func):
# 	def wrapper():
# 		original_result = func()
# 		modi = original_result.upper()
# 		return modi
# 	return wrapper
# def greeting():
# 	return 'Hello'

import functools

def uppercase(func):
	@functools.wraps(func)
	def wrapper():
		original_result = func()
		modi = original_result.upper()
		return modi
	return wrapper
def greetings():
	return 'hello'