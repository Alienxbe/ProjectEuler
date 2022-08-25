def	strip_name(name: str):
	return (name.strip('"'))

def	get_name_value(name: str):
	return (sum([(ord(i) - ord('A') + 1) for i in name]))

def	main():
	with open("names.txt", 'r') as file:
		names = list(map(strip_name, file.read().split(',')))
		names.sort()
		total = sum([get_name_value(name) * (names.index(name) + 1) for name in names])
		print(total)

main()