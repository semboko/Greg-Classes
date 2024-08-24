
def is_prime(n):
    d = 2
    while d < n:
        if n % d == 0:
            return False
        d = d + 1
    return True


n = 2
while n < 1000:
    if is_prime(n):
        print(n)
    n = n + 1
