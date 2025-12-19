N = int(input("Enter the power value N: "))

if N < 0 or N >= 31:
    print("Please enter N such that 0 <= N < 31")
else:
    i = 0
    power = 1  

    while i <= N:
        print("2 ^", i, "=", power)
        power = power * 2 
        i = i + 1
