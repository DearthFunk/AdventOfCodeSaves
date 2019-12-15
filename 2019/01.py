import math

# import requests
# url = "https://adventofcode.com/2019/day/1/input"
# response = requests.get(url)
# print(response.status_code)
# print(response.content)

arr = [
	81893,
	122450,
	81968,
	135462,
	127082,
	94016,
	100999,
	88954,
	111500,
	89232,
	149706,
	70377,
	114053,
	116799,
	57368,
	117222,
	134050,
	58097,
	113145,
	67710,
	115082,
	109484,
	76183,
	87768,
	85164,
	141183,
	120410,
	85101,
	139190,
	120483,
	89111,
	122940,
	103010,
	127018,
	85178,
	73893,
	145037,
	115786,
	149613,
	122956,
	96325,
	123513,
	126850,
	124733,
	116615,
	131598,
	94544,
	94431,
	97681,
	86617,
	56739,
	104904,
	129964,
	80862,
	92125,
	127108,
	110565,
	131296,
	88192,
	81824,
	134198,
	87363,
	122455,
	123441,
	60907,
	95023,
	113940,
	98328,
	79989,
	146133,
	122356,
	70932,
	106379,
	125641,
	124905,
	89699,
	129133,
	112173,
	127629,
	135485,
	140068,
	95229,
	141276,
	109807,
	69951,
	100792,
	62683,
	145565,
	149063,
	99523,
	88881,
	64337,
	145012,
	142380,
	60028,
	131565,
	53041,
	88489,
	81712,
	132728,
]


def get_fuel_based_on_mass(mass):
	return math.floor(mass/3) - 2


def part_one(data):
	total = 0
	for mass in data:
		fuel = get_fuel_based_on_mass(mass)
		total += fuel

	return total


def part_two(data):
	total = 0
	for mass in data:
		fuel = get_fuel_based_on_mass(mass)
		while fuel > 0:
			total += fuel
			fuel = get_fuel_based_on_mass(fuel)

	return total


print('PART 1: ', part_one(arr))
print('PART 2: ', part_two(arr))




