"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    
    if number_of_primes >= 1:
        list = [2]
        while (len(list) < number_of_primes):
            testNum = 3
            for i in range(2, testNum//2):
                if (testNum % i) == 0:
                    break
                else :
                    list.append(testNum)
    else:
        raise ValueError

    return list
