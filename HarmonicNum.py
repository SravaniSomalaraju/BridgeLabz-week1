N = int(input("Enter the harmonic value N: "))

if N == 0:
    print("N should not be zero")
else:
    harmonic = 0.0   

    for i in range(1, N + 1):
        harmonic = harmonic + (1 / i)

    print("The", N, "th Harmonic Value is:", harmonic)
