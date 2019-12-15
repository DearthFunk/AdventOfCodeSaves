def fn_add(var1, var2):
	return var1 + var2


def fn_mul(var1, var2):
	return var1 * var2


def fn_default(var1, var2):
	return


codes = {
	"99": fn_add,
	"1": fn_add,
	"2": fn_mul
}

################################################################
################################################################


def int_code_program(memory, result):
	def terminate_program():
		return "terminator!"

	def chunks(l, n):
		n = max(1, n)
		return (l[i:i + n] for i in range(0, len(l), n))

	def exec_instruction(code, noun, verb, idx):
		val1 = active_mem[noun]
		val2 = active_mem[verb]
		active_mem[idx] = codes[str(code)](val1, val2)

	def process_instruction(comm):
		if comm[0] == 99:
			terminate_program()
			return

		if str(comm[0]) in codes:
			exec_instruction(*comm)
		else:
			terminate_program()
			return

	def process_instructions(instructions):
		for instruction in instructions:
			try:
				process_instruction(instruction)
			except Exception as ex:
				print(ex)
				raise Exception("---> BROKE Command")

	def run():
		nonlocal active_mem
		for verb in range(100):
			for noun in range(100):
				active_mem = memory.copy()
				active_mem[1] = noun
				active_mem[2] = verb
				process_instructions(chunks(active_mem, 4))
				if active_mem[0] == result:
					print(100 * noun + verb)
					return 100 * noun + verb

		return "nothing found"

	active_mem = []
	run()


#############################################
#############################################

result = 19690720
data = [
	1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 9, 1, 19, 1, 19, 5, 23, 1, 9, 23, 27, 2, 27, 6, 31, 1, 5, 31, 35,
	2, 9, 35, 39, 2, 6, 39, 43, 2, 43, 13, 47, 2, 13, 47, 51, 1, 10, 51, 55, 1, 9, 55, 59, 1, 6, 59, 63, 2, 63, 9, 67,
	1, 67, 6, 71, 1, 71, 13, 75, 1, 6, 75, 79, 1, 9, 79, 83, 2, 9, 83, 87, 1, 87, 6, 91, 1, 91, 13, 95, 2, 6, 95, 99, 1,
	10, 99, 103, 2, 103, 9, 107, 1, 6, 107, 111, 1, 10, 111, 115, 2, 6, 115, 119, 1, 5, 119, 123, 1, 123, 13, 127, 1,
	127, 5, 131, 1, 6, 131, 135, 2, 135, 13, 139, 1, 139, 2, 143, 1, 143, 10, 0, 99, 2, 0, 14, 0
]
int_code_program(data, result)
