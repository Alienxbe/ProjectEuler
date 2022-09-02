from math import sqrt


def	get_proper_div(n: int):
	return ([i for i in range(1, n // 2 + 1) if (n % i == 0)])

def sumofFactors(n):
	 
	# Traversing through all
	# prime factors
	res = 1
	for i in range(2, int(sqrt(n) + 1)):
		
		curr_sum = 1
		curr_term = 1
		
		while n % i == 0:
			
			n = n / i;
 
			curr_term = curr_term * i;
			curr_sum += curr_term;
			 
		res = res * curr_sum
	 
	# This condition is to handle the
	# case when n is a prime number
	# greater than 2
	if n > 2:
		res = res * (1 + n)
	return res;

def	is_perfect(n: int):
	return (sumofFactors(n) - n == n)

def	is_deficient(n: int):
	return (sumofFactors(n) - n < n)

def	is_abundant(n: int):
	return (sumofFactors(n) - n > n)

def	main():
	abundants = [i for i in range(1, 28123) if is_abundant(i)]
	res_sum = []

	for i in range(len(abundants)):
		for j in range(i, len(abundants)):
			if (abundants[i] + abundants[j] > 28123):
				break
			print(i, j, len(res_sum))
			if (abundants[i] + abundants[j] not in res_sum):
				res_sum.append(abundants[i] + abundants[j])
	res_sum.sort()


main()