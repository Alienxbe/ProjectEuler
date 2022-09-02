# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mykman <mykman@student.s19.be>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/01 07:13:17 by mykman            #+#    #+#              #
#    Updated: 2022/09/01 07:45:47 by mykman           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	getNextDigit(n, d, rec_coutn, rec_max) -> str:
	if (rec_coutn == rec_max):
		return ""
	n *= 10
	digit = n // d
	rest = n % d
	return str(digit) + getNextDigit(rest, d, rec_coutn + 1, rec_max)

def	findPatern(digits: str) -> str:
	pass

def	main():
	for i in range(2, 11):
		digits = getNextDigit(1, i, 0, 500)
		print(f"1/{i} = {digits.rstrip('0')}")

main()
