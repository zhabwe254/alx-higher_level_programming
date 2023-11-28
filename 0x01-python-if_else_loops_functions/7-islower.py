#!/usr/bin/python3

def islower(c):
	return ord('a') <= ord(c) <= ord('z')

# Test cases
print("a is", "lower" if islower("a") else "upper")
print("H is", "lower" if islower("H") else "upper")
print("A is", "lower" if islower("A") else "upper")
print("3 is", "lower" if islower("3") else "upper")
print("g is", "lower" if islower("g") else "upper")
