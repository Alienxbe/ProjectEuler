numbers_units = [
	"zero",
	"one",
	"two",
	"three",
	"four",
	"five",
	"six",
	"seven",
	"eight",
	"nine",
	"ten",
	"eleven",
	"twelve",
	"thirteen",
	"fourteen",
	"fifteen",
	"sixteen",
	"seventeen",
	"eighteen",
	"nineteen"
]

numbers_ten = [
	"twenty",
	"thirty",
	"forty",
	"fivty",
	"sixty",
	"seventy",
	"eighty",
	"ninety"
]

def numbers_19(n):
	return (numbers_units[n])

def numbers_99(n):
	if (n < 20):
		return (numbers_19(n))
	if (n % 10 == 0):
		return (numbers_ten[n // 10 - 2])
	return (numbers_ten[(n // 10) - 2] + " " + numbers_19(n % 10))

def numbers_999(n):
	if (n < 100):
		return (numbers_99(n))
	if (n % 100 == 0):
		return (numbers_units[n // 100] + " hundred")
	return (numbers_units[n // 100] + " hundred and " + numbers_99(n % 100))

def number_to_str(n):
	return (numbers_999(n))

def get_len(n):
	return (len(("".join(number_to_str(n).split(" ")))))

def main():
	count = 0
	for i in range(1, 1000):
		count += get_len(i)
		print(i, ":", number_to_str(i), get_len(i), "(" + str(count) + ")")
	print(count + len("onethousand"))

main()
