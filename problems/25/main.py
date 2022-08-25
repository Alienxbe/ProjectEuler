fibo = [0, 1, 1]

def	fibonnacy(i: int):
	if (i < len(fibo)):
		return (fibo[i])
	n = fibonnacy(i - 1) + fibonnacy(i - 2)
	fibo.append(n)
	return (n)

def main():
	i = 1
	while (len(str(fibonnacy(i))) != 1000):
		print(i, len(str(fibonnacy(i))), fibonnacy(i))
		i += 1
	print(i)

main()
