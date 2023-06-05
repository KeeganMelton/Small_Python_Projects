
# checks to see if the entered number is prime by looping through all number from 2 to the entered number
def prime_checker(n):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
    if prime == True:
        print(f"{n} is a prime number")
    else:
        print(f" {n} is not a prime number")


check_again = True

# loops until the user does not want to check another number
while check_again == True:
    n = int(input("Enter a number to check: "))
    prime_checker(n)
    again = input("Do you want to check another number (y\\n)? ").lower()
    if again == 'y':
        check_again = True
    else:
        check_again = False