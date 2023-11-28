#!/usr/bin/python3

for tens in range(10):
	for units in range(10):
		print(f"{tens}{units}", end=", " if tens != 9 or units != 9 else "\n")
