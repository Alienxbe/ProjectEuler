def	get_proper_div(n: int):
	return ([i for i in range(1, n // 2 + 1) if (n % i == 0)])

def	is_perfect(n: int):
	return (sum(get_proper_div(n)) == n)

def	is_deficient(n: int):
	return (sum(get_proper_div(n)) < n)

def	is_abundant(n: int):
	return (sum(get_proper_div(n)) > n)

def get_abundant_sum(n: int, abundant: list):
	if (len(abundant) == 0):
		return (False)
	for i in range(len(abundant)):
		a = abundant[i]
		for j in range(len(abundant)):
			b = abundant[j]
			if (a + b == n):
				return (True)
	return (False)

def is_abundant_sum(n: int, abundant:list):
	return (get_abundant_sum(n, abundant) != False)

def	main():
	abundant = []
	tot = 0
	for i in range(1, 28123):
		if (is_abundant(i)):
			abundant.append(i)
		elif (get_abundant_sum(i, abundant) == False):
			tot += i
			print(i, tot, len(abundant))
	print(tot)

main()