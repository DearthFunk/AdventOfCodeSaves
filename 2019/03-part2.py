import sys

directions = {
	'R': (1, 0),
	'L': (-1, 0),
	'U': (0, 1),
	'D': (0, -1)
}


def get_manhattan_distance(line1, line2):
	def get_points_from_path(path):
		x = 0
		y = 0
		step = 0
		points = {}
		for segment in path:
			dx, dy = directions[segment[0]]
			for item in range(int(segment[1:])):
				x += dx
				y += dy
				step += 1
				if (x, y) not in points:
					points[(x, y)] = step

		return points

	def get_point_intersects(points1, points2):
		return [point for point in points1 if point in points2]

	wire1_points = get_points_from_path(line1)
	wire2_points = get_points_from_path(line2)

	intersection_points = get_point_intersects(wire1_points, wire2_points)

	return min(wire1_points[point] + wire2_points[point] for point in intersection_points)


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

print('610: ', result_1)
print('410: ', result_2)
print(' 30: ', result_3)

f = open("data.txt", "r")
data = f.read().split('\n')
line1 = data[0].split(',')
line2 = data[1].split(',')
result_4 = get_manhattan_distance(line1, line2)
print('------------')
print(result_4)