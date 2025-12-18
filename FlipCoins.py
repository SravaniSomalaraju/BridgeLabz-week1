import random   

n = int(input("Enter number of times to flip the coin: "))

if n <= 0:
    print("Please enter a positive integer")
else:
    heads = 0
    tails = 0

    for i in range(n):
        r = random.random()   

        if r < 0.5:
            tails += 1
        else:
            heads += 1

    heads_percentage = (heads / n) * 100
    tails_percentage = (tails / n) * 100

    print("Heads percentage:", heads_percentage, "%")
    print("Tails percentage:", tails_percentage, "%")
