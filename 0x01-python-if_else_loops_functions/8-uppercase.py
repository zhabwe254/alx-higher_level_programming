#!/usr/bin/python3

def uppercase(s):
for char in s:
	upper_char = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
		print(upper_char, end="")
		print()

# Test cases
uppercase("best")
uppercase("Best School 98 Battery street")
