month_30 = [
	9,
	4,
	6,
	11
]

week_days = [
	"Monday",
	"Thuesday",
	"Wednesday",
	"Thursday",
	"Friday",
	"Saturday",
	"Sunday"
]

months = [
	"Jan",
	"Feb",
	"Mar",
	"Apr",
	"Mai",
	"Jun",
	"Jul",
	"Aug",
	"Sep",
	"Oct",
	"Nov",
	"Dec"
]

def is_leap_year(year: int):
	if (year % 400 == 0):
		return (True)
	if (year % 4 == 0 and year % 100 != 0):
		return (True)
	return (False)

def	get_month_max_day(month: int, year: int):
	if (month == 2):
		if (is_leap_year(year)):
			return (29)
		return (28)
	if (month in month_30):
		return (30)
	else:
		return (31)

def get_next_weekday(day: int):
	if (day == 6):
		return (0)
	return (day + 1)

def get_next_day(day: int, month: int, year: int):
	if (day == get_month_max_day(month, year)):
		return (1)
	return (day + 1)

def get_next_month(month: int):
	if (month == 12):
		return (1)
	return (month + 1)

def main():
	weekday = week_days.index("Sunday")
	day = 31
	month = 12
	year = 2000

	while (year != 2023 or day != 24 or month != 8):
		if (day == 30 and month == 10):
			print(f"{week_days[weekday]}, {day} {months[month - 1]} {year}")
		weekday = get_next_weekday(weekday)
		day = get_next_day(day, month, year)
		if (day == 1):
			month = get_next_month(month)
			if (month == 1):
				year += 1

main()