import math

# import requests
# url = "https://adventofcode.com/2019/day/2/input"
# response = requests.get(url)
# print(response.status_code)
# print(response.content)

data = [
	1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,9,23,27,2,27,6,31,1,5,31,35,2,9,35,39,2,6,39,43,2,43,13,47,2,13,47,51,1,10,51,55,1,9,55,59,1,6,59,63,2,63,9,67,1,67,6,71,1,71,13,75,1,6,75,79,1,9,79,83,2,9,83,87,1,87,6,91,1,91,13,95,2,6,95,99,1,10,99,103,2,103,9,107,1,6,107,111,1,10,111,115,2,6,115,119,1,5,119,123,1,123,13,127,1,127,5,131,1,6,131,135,2,135,13,139,1,139,2,143,1,143,10,0,99,2,0,14,0
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

print(data)




