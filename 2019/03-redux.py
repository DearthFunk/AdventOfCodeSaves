import datetime
from sympy import Point, Line, Segment


def get_manhattan_distance(line1, line2):
	def get_line_segments(line_data):
		def adjust_pos(point, cmd):
			direction = cmd[0]
			distance = int(cmd[1:])
			x = point[0]
			y = point[1]
			if direction == 'R':
				return x + distance, y
			elif direction == 'L':
				return x - distance, y
			elif direction == 'U':
				return x, y + distance
			elif direction == 'D':
				return x, y - distance

		line_segments = []
		p1 = (0, 0)
		p2 = (0, 0)
		for index, cmd in enumerate(line_data):
			p2 = adjust_pos(p2, cmd)
			seg = Segment(
				Point(p1[0], p1[1]),
				Point(p2[0], p2[1])
			)
			line_segments.append(
				(seg, cmd)
			)
			p1 = p2

		return line_segments

	def get_line_intersections(set_a, set_b):
		intersects = []
		for line_a in set_a:
			l1 = line_a[0]
			print(l1)
			for line_b in set_b:
				l2 = line_b[0]
				point_of_intersection = l1.intersection(l2)
				print('   ', l2, point_of_intersection)
				if len(point_of_intersection) == 0:
					continue
				intersects.append(point_of_intersection)

		return intersects

	def get_point_distances(data):
		res = []
		for point in data:
			# Note: dist != distance between points, but distance travelled
			distance_traveled = abs(point[0].x) + abs(point[0].y)
			res.append(distance_traveled)
		return res

	print_steps = True
	if print_steps:
		print('--- data -------------------')
		print(line1)
		print(line2)

	line1_segments = get_line_segments(line1)
	line2_segments = get_line_segments(line2)
	if print_steps:
		print('--- segments ---------------')
		print(line1_segments)
		print(line2_segments)

	intersections = get_line_intersections(line1_segments, line2_segments)
	# first intersection is always 0,0
	intersections.pop(0)
	if print_steps:
		print('--- intersections ----------')
		print(intersections)

	distances = get_point_distances(intersections)
	if print_steps:
		print('--- distances -------------')
		print(distances)
		print('=============================')
		print('')
		print('')

	return min(distances)


################################################

f = open("data.txt", "r")
data = f.read().split('\n')
line1 = data[0].split(',')
line2 = data[1].split(',')
start_date_time = datetime.datetime.now()
result = get_manhattan_distance(
	line1,
	line2,
)
print('start: ', start_date_time)
print('  end: ', datetime.datetime.now())
print('RESULT:', result)

"""
result_1 = get_manhattan_distance(
	['R75','D30','R83','U83','L12','D49','R71','U7','L72'],
	['U62','R66','U55','R34','D71','R55','D58','R83']
)
result_2 = get_manhattan_distance(
	['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],
	['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
)
result_3 = get_manhattan_distance(
	['R8','U5','L5','D3'],
	['U7','R6','D4','L4']
)
print('159: ', result_1)
print('135: ', result_2)
print('  6: ', result_3)
"""