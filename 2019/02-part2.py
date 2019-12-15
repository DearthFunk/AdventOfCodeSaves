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
	1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,1,13,23,27,1,6,27,31,2,31,13,35,1,9,35,39,2,39,13,43,1,43,10,47,1,47,13,51,2,13,51,55,1,55,9,59,1,59,5,63,1,6,63,67,1,13,67,71,2,71,10,75,1,6,75,79,1,79,10,83,1,5,83,87,2,10,87,91,1,6,91,95,1,9,95,99,1,99,9,103,2,103,10,107,1,5,107,111,1,9,111,115,2,13,115,119,1,119,10,123,1,123,10,127,2,127,10,131,1,5,131,135,1,10,135,139,1,139,2,143,1,6,143,0,99,2,14,0,0
]
int_code_program(data, result)
