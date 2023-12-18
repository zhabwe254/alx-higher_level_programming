#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
	result_list = []
	for i in range(list_length):
	try:
	result = my_list_1[i] / my_list_2[i]
	except (ZeroDivisionError, TypeError):
		print("wrong type")
		result = 0
	except IndexError:
		print("out of range")
		result = 0
	finally:
		result_list.append(result)
	return result_list

if __name__ == "__main__":
	my_l_1 = [10, 8, 4]
	my_l_2 = [2, 4, 4]
	result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
	print(result)

	print("--")

	my_l_1 = [10, 8, 4, 4]
	my_l_2 = [2, 0, "H", 2, 7]
	result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
	print(result)
