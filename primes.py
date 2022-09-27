"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes<=0:
        raise ValueError("the number of primes must be greater than 0")
    numbers = [2]
    list = []
    counter=0
    while counter<number_of_primes:
        if counter==0:
            list.append(2)
            counter+=1
        else:
            list.append(findPrime(list[len(list)-1], numbers))
            counter+=1
    return list

def findPrime(start, numbers):
    found = False
    num = start
    while not found:
        num+=1
        if not divisible(num, numbers):
            found = True
        numbers.append(num)
    return num

def divisible(num, numbers):
    result = False
    counter = len(numbers)-1
    while counter>=0:
        # print(num)
        # print(numbers[counter])
        # print(num%numbers[counter])
        if num%numbers[counter] == 0:
            result = True
            break
        else:
            counter-=1
    return result
