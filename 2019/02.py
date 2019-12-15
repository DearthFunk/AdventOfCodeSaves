import math

# import requests
# url = "https://adventofcode.com/2019/day/2/input"
# response = requests.get(url)
# print(response.status_code)
# print(response.content)

data = [
	1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,1,13,23,27,1,6,27,31,2,31,13,35,1,9,35,39,2,39,13,43,1,43,10,47,1,47,13,51,2,13,51,55,1,55,9,59,1,59,5,63,1,6,63,67,1,13,67,71,2,71,10,75,1,6,75,79,1,79,10,83,1,5,83,87,2,10,87,91,1,6,91,95,1,9,95,99,1,99,9,103,2,103,10,107,1,5,107,111,1,9,111,115,2,13,115,119,1,119,10,123,1,123,10,127,2,127,10,131,1,5,131,135,1,10,135,139,1,139,2,143,1,6,143,0,99,2,14,0,0
]


def fn_add(var1, var2):
	return var1 + var2


def fn_mul(var1, var2):
	return var1 * var2


def fn_default(var1, var2):
	return


codes = {
	"99": fn_default,
	"1": fn_add,
	"2": fn_mul
}


def get_val_at_index(arr, index):
	i = 0
	while i < len(arr):
		op_code = arr[i]
		if op_code == 99:
			break;
		idx_1 = arr[i+1]
		idx_2 = arr[i+2]
		idx_change = arr[i+3]
		op_code = str(op_code)
		if op_code in codes:
			arr[idx_change] = codes[op_code](arr[idx_1], arr[idx_2])

		i += 4

	return arr[index]


# 6568671
data[1] = 12
data[2] = 2

print(get_val_at_index(data, 0))




