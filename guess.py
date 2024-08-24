from random import randint


number = randint(0, 100)

x = 0
while x < 7:
    try:
        n = int(input())
    except ValueError:
        print("Only numbers are accepted!")

    if n == number:
        print("The number is correct!")
        exit()
    if n < number:
        print("Your number is smaller")
    if n > number:
        print("Your number is greater")

    x = x + 1

print("The number wasn't guessed. Game over!")
