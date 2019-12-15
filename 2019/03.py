# https://adventofcode.com/2019/day/3/input


def get_manhattan_distance(line1, line2):
	def parse_line(line_data):
		x = 0
		y = 0
		pos = {'x': x, 'y': y, 'msg': line_data[0]}
		items = [pos]

		# we enumerate starting at index 1 and then grab the previous message
		# benefit is we can attach the msg command to the prev index
		# so if the first 2 commands are  R10 U10 xxxx
		# you can read it step by step [{0,0,'R10'}, {10,0,'U10}, {10,10,xxxxx}]
		# make it easy to read
		# just have to remember the applied result of the message is the x/y at n+1
		prev_msg = ''
		for index, msg in enumerate(line_data[1:]):
			prev_msg = line_data[index]
			direction = prev_msg[0]
			distance = int(prev_msg[1:])
			res = get_pos(direction, distance, x, y)
			pos = {'x': res[0], 'y': res[1], 'msg': msg}
			items.append(pos)

		# need to calculate last command now
		# ???

		return items

	def get_pos(direction, distance, x, y):
		if direction == 'R':
			x += distance
		elif direction == 'L':
			x -= distance
		elif direction == 'U':
			y += distance
		elif direction == 'D':
			y -= distance
		return x, y

	#https://stackoverflow.com/questions/3838329/how-can-i-check-if-two-segments-intersect
	def ccw(a, b, c):
		return (c['y'] - a['y']) * (b['x'] - a['x']) > (b['y'] - a['y']) * (c['x'] - a['x'])

	def intersect(a, b, c, d):
		return ccw(a, c, d) != ccw(b, c, d) and ccw(a, b, c) != ccw(a, b, d)

	def print_line_data(line_strings, line_data):
		print(line_strings)
		for line in line_data:
			print(line)
		print('-----')
		print(len(line_strings), len(line_data))
		print('-----')

	line1_data = parse_line(line1)
	#line2_data = parse_line(line2)

	print_line_data(line1, line1_data)
	#print_line_data(line2, line2_data)
"""
	i = 0
	while i < len(line1_data):
		j = 0
		while j < len(line2_data):
			l1p1 = line1_data[i]
			l1p2 = line1_data[i+1]
			l2p1 = line2_data[j]
			l2p2 = line2_data[j+1]
			#http: // openbookproject.net / thinkcs / python / english3e / dictionaries.html
			lines_intersect = intersect(l1p1, l1p2, l2p1, l2p2)

			if lines_intersect:
				print(l1p1, l1p2, l2p1, l2p2)

			j += 2
		i += 2
"""







################################################


f = open("data.txt", "r")
data = f.read().split('\n')
line1 = data[0].split(',')
line2 = data[1].split(',')
get_manhattan_distance(
	line1,
	line2,
)

