def	get_proper_div(n: int):
	return ([i for i in range(1, n // 2 + 1) if (n % i == 0)])

def	is_amicable(a: int):
	b = sum(get_proper_div(a))
	return (a != b and sum(get_proper_div(b)) == a)

def	main():
	amicables = [i for i in range(1, 10000) if is_amicable(i)]
	print(amicables)
	print(sum(amicables))

main()
