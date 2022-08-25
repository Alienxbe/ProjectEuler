def swap(l: list, i: int, j: int):
	l[i] ^= l[j]
	l[j] ^= l[i]
	l[i] ^= l[j]
	return (l)

def	print_perm(l: list, n: int, do_print: bool):
	if (len(l) < n or n < 1):
		raise KeyError
	elif (n == 1):
		if (do_print):
			print("".join(list(map(str, l))))
	else:
		for i in range(n):
			print_perm(l, n - 1, n % 2 == 0)
			swap(l, -n, -(n - i - 1))

def	main():
	l = [0, 1, 2]
	print_perm(l, len(l), True)

main()

# 012
## Swap -2 & -1
# 021
# 102
# 120
# 201
# 210

# 0123
# 0132
# 0213
# 0231
# 0312
# 0321
# 1023

