year = int(input("Enter a year: "))

## divided by 100 means centurt year (end with 00)
# century year divided by 400 is Leap year
if (year % 400 == 0) and (year % 100 == 0):
	print("{0} is a leap year" .format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 == 0) and (year % 100 != 0):
	print("{0} is a leap year".format(year))

# if not divided by bith 400 (century year) and 4 (not century year)
# year is not leap year
else:
	print("{0} is not leap year".format(year)) 


