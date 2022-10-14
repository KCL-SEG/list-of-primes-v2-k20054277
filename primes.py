"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    
    if number_of_primes >= 1:
        list = [2]
        testNum = 3
        
        while (len(list) < number_of_primes):
            prime = True
            for i in range(2, testNum):
                if (testNum % i) == 0:
                    prime = False
                    break
                
            if prime == True:
                list.append(testNum)
            testNum= testNum+1
    else:
        raise ValueError

    return list
