
import math
number_of_primes = 1
sum_of_log = 0

def itsPrimef(current_number):
    current_prime = 2
    while not current_number % current_prime == 0:
        current_prime = current_prime + 1
    if current_number == current_prime:
        global prime
        prime = current_number
        global number_of_primes
        number_of_primes = number_of_primes + 1
        global sum_of_log
        sum_of_log = math.log(prime) + sum_of_log
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

number = int(input("This program calculate the sum of log of all primes near an aleatory number, and the ratio between this elements. Type a number. "))
if number >= 1:
    number_of_primesf(number)
    print("Number of primes", number_of_primes)
    print("Ratio between the number and the sum of logarithms of a prime", sum_of_log/number)
if number <= 0:
    print("0")

