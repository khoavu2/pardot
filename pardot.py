"""
You are given a function 'secret()' that accepts a single integer parameter and returns an integer. 
In your favorite programming language, write a command-line program that takes one command-line 
argument (a number) and determines if the secret() function is additive [secret(x+y) = secret(x) + secret(y)], 
for all combinations x and y, where x and y are all prime numbers less than the number passed 
via the command-line argument. Describe how to run your examples. 
Please generate the list of primes without using built-in functionality.
"""

import sys
import math

def isPrime(n):
    upperLimit = math.sqrt(n)
    i = 2

    while i <= upperLimit:
        if n % i == 0:
            return False
        i += 1
        
    return True


def primeNumbersLessThan(n):
    primes = []

    count = 2

    while count <= n:
        if isPrime(count):
            primes.append(count)
        count += 1
    
    return primes

def check_additive(func, n):
    primes = primeNumbersLessThan(n)
    #print func(n)

    for num in primes:
        for numCopy in primes:
            #print num, numCopy
            if func(num + numCopy) != func(num) + func(numCopy):
                return False

    return True

#Additive test function
def testFunc1(n):
    return n * 4

#None additive test function
def testFunc2(n):
    return n + 3

#None additive test function
def testFunc3(n):
    return 1

#None additive test function
def testFunc4(n):
    return n * 2 + 1

#Additive test function
def testFunc5(n):
    return n

def main():
    args = sys.argv[1:]

    if not args:
        print 'usage: filename [number]'
        sys.exit(1)
    
    number = int(sys.argv[1])
    
    test = testFunc1
    #test = testFunc2
    #test = testFunc3
    #test = testFunc4
    #test = testFunc5

    if check_additive(test, number):
        print "secret() function is additive!"
    else:
        print "secret() function is not additive!"

    return

if __name__ == '__main__':
    main()