def	split_int(string):
	return (list(map(int, string.split())))

def calc_path(triangle, pos=(0, 0), count=0):
	val = 0
	try:
		val = triangle[pos[1]][pos[0]]
	except IndexError:
		return (0)

	left = calc_path(triangle, (pos[0], pos[1] + 1))
	right = calc_path(triangle, (pos[0] + 1, pos[1] + 1))
	if (left > right):
		print("left")
		return (val + left)
	print("right")
	return (val + right)

def main():
	with open("triangle.txt", 'r') as file:
		triangle = list(map(split_int, file.read().splitlines()))
		print(triangle)
		print(calc_path(triangle))

main()
