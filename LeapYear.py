year = int(input("Enter a 4-digit year: "))

if year < 1000 or year > 9999:
    print("Please enter a valid 4-digit year")
else:
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year, "is a Leap Year")
    else:
        print(year, "is NOT a Leap Year")
