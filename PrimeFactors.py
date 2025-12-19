N = int(input("Enter a number to find its prime factors: "))

if N <= 1:
    print("Please enter a number greater than 1")
else:
    i = 2   
    print("Prime factors are:")

    while i * i <= N:
        while N % i == 0:
            print(i)
            N = N // i  
        i = i + 1

    if N > 1:
        print(N)
