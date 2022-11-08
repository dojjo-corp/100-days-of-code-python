# Write your code below this line

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            print("It's not a prime number")
    if is_prime == True:
        print("It's a prime number")

# Don't change the code below this line

n = int(input("Check this number: "))
prime_checker(number=n)
