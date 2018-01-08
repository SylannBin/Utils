#!/usr/bin/python
"""
This script calculates the prime numbers
up to a user defined limit or to the default 10,000th.
"""

import sys
from time import clock
from math import sqrt

def Recalibrate(LastNum):
    """
    Picks the proper limit number based on LastNum
    in order to obtain a multiple of 6.
    """
    # The LastNum must be a multiple of 6!!
    # This selects the proper case in the dictionnary based on LastNum % 6
    # Example: if Num % 6 == 2, add 4
    return {
        0: LastNum,
        1: LastNum + 5,
        2: LastNum + 4,
        3: LastNum + 3,
        4: LastNum + 2,
        5: LastNum + 1
        }[LastNum % 6]

def BuildInitialList(LastNum):
    """
    Builds an array of boolean values (0/1) filled
    with 1/3 of the provided LastNum, reduced by 1.
    First element is 0, all other elements are 1.
    """
    return [0] + [1] * (int(LastNum / 3) - 1)

def GetClearingRange(LastNum):
    """
    Builds the list of consecutive numbers after which
    enough prime numbers have been identified to clear
    all other non prime multiples.
    """
    return range(int(sqrt(LastNum) / 3) + 1)

def GetClearedRange(LastNum):
    """
    Builds a list of numbers that is large enough based
    on provided number.
    """
    return range(1, int(LastNum / 3))

def U(n):
    """
    Effectively reduce the numbers that we bother to test
    """
    return 3*n +1 |1

def V(n):
    """
    U(n)²
    """
    return U(n)**2

def W(n):
    """
    U(n)² + 4U(n) - 2U(n) (only if n is odd)
    or
    U(n)² + 4U(n)
    """
    return V(n) + 4*U(n) -2*(n&1)*U(n)

def GetEnoughZeros(LastNum, n, F):
    """
    Generates a list containing only zeros.
    Populates it with the exact needed amount of elements
    based on LastNum.
    F is a function V or W.
    """
    return int((int(LastNum /6) -int(F(n) /6) -1) /U(n) +1)

def PrimeGenerator(LastNum):
    """
    Builds and updates the list of possible prime numbers
    until a number is found to be prime and gets yielded.
    """
    LastNum = Recalibrate(LastNum)
    # Build boolean list
    CouldBePrime = BuildInitialList(LastNum)
    # Clean the CouldBePrime list from composite numbers (applying eratosthene's sieve)
    for n in GetClearingRange(LastNum):
        if CouldBePrime[n]:
            # Target the current third of V(n) (same with W(n))
            # aswell as all the numbers at each "2U(n)" step
            # Ex: U(n) = 11, select all numbers each 22 elements of the list
            # Replace all these elements with the exact needed amount of values (based on LastNum)
            CouldBePrime[int(V(n)/3)::2*U(n)] = [0]*GetEnoughZeros(LastNum, n, V)
            CouldBePrime[int(W(n)/3)::2*U(n)] = [0]*GetEnoughZeros(LastNum, n, W)
    # First eliminate 2 and 3 (we know them well :-p)
    yield 2
    yield 3
    # For the limited range based on LastNum
    for n in GetClearedRange(LastNum):
        # only if still not eliminated previously
        if CouldBePrime[n]:
            # and only those uNum values (see previosuly)
            yield U(n)

def SequentialPrint(LastNumber, PrimeCount):
    """
    Print the list of prime numbers found by the
    PrimeGenerator function to the console screen.
    """
    for i, j in enumerate(PrimeGenerator(LastNumber)):
        print("{}:{}".format(i + 1, j))
        if i + 1 == PrimeCount:
            break

def Main():
    """
    This script displays all found prime numbers from 2 to the selected amount.
    Expected arguments:
    - 1: Max range of numbers to evaluate (default 1,000,000)
    - 2: Max ammount of prime numbers to print (default 10,000)
    """
    LastNumber = 1000000
    PrimeCount = 10000
    try:
        LastNumber = int(sys.argv[1])
    except IndexError:
        print("No value provided. Limit set to default: 1,000,000")
    except ValueError:
        print("Non int value provided: {0}.\
        Limit set to default: 1,000,000".format(sys.argv[1]))
    try:
        PrimeCount = int(sys.argv[2])
    except IndexError:
        print("No value provided. Count set to default: 10,000")
    except ValueError:
        print("Non int value provided: {0}.\
        Count set to default: 10,000".format(sys.argv[2]))

    start = clock()
    SequentialPrint(LastNumber, PrimeCount)
    end = clock()

    print("\nNumbers found in", round((end - start), 5), "secs")

if __name__ == '__main__':
    Main()
