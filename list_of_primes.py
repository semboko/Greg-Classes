n = 2

upper_limit = 100

while n <= upper_limit:
    x = 2
    is_prime = True
    while x < n:
        if n % x == 0:
            is_prime = False
            break
        x = x + 1

    if is_prime is True:
        print(n)

    n = n + 1
