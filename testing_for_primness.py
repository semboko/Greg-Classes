n = 1333

x = 2

while x < n:
    if n % x == 0:
        print("n is not prime, it is divisible by", x)
        exit()
    x = x + 1

print("n is prime")
