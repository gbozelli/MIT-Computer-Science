
number_of_primes = 0

def itsPrimef(current_number):
    current_prime = 2
    while not current_number % current_prime == 0:
        current_prime = current_prime + 1
    if current_number == current_prime:
        global prime
        prime = current_number
        global number_of_primes
        number_of_primes = number_of_primes + 1
def biggest_primef(x):
    current_number = 1
    while current_number != x:
        current_number = current_number + 1
        itsPrimef(current_number) 
        if x == current_number:
            return prime

def number_of_primesf(number):
    biggest_primef(number)
    return number_of_primes 

number = int(input("This program calculate the biggest prime near an aleatory number. Type a number. "))
number_of_primesf(number)
print(prime)

