def is_leap_year(year):
    # Leap years are either divisible by 4 and not divisible by 100
    # or divisible by 400.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Input from the user
year = int(input("Enter a year: "))

if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


#OUTPUT

#Enter a year: 2014
#2014 is not a leap year

#Enter a year: 2016
#2016 is a leap year

