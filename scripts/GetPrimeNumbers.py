"""
This script calculates the prime numbers
up to a user defined limit.
"""

from time import clock
from math import sqrt

def Recalibrate(Num):
    """
    Determinantes the proper limit number corresponding to the
    multiples and to the provide parameter.
    """
    # La limite doit être divisible par 6 !!
    # exemple si le reste de Num/6 est 2, il manque 4 pour obtenir un nombre divisible par 6
    # [Num%6] est utilisé comme indice du dictionnaire implicitement déclaré à sa gauche
    return {
        0: Num,
        1: Num + 5,
        2: Num + 4,
        3: Num + 3,
        4: Num + 2,
        5: Num + 1
        }[Num % 6]

def BuildInitialList(length):
    """
    Builds an array of boolean values filled with enough
    elements to match length parameter.
    At the begining, 'even' elements are set to False
    while odd elements are set to True.
    """
    return [0] + [1] * (int(length / 3) - 1)

def GetClearingRange(number):
    """
    Builds the list of consecutive numbers after which
    enough prime numbers have been idetified to clear
    all other non prime multiples.
    """
    return range(int(sqrt(number) / 3) + 1)

def GetClearedRange(number):
    """
    Builds a list of numbers that is large enough based
    on provided number.
    """
    return range(1, int(number / 3))

def PrimeGenerator(LastNum):
    """
    Builds and updates the list of possible prime numbers
    until a number is found to be prime and gets yielded.
    """
    LastNum = Recalibrate(LastNum)
    # Création de la liste globale
    CouldBePrime = BuildInitialList(LastNum)
    # Début du nettoyage de CouldBePrime
    for Num in GetClearingRange(LastNum):
        if CouldBePrime[Num]:
            uNum = 3 * Num +1 |1
            vNum = uNum * uNum
            wNum = vNum + uNum * (4 - 2 * (Num & 1))
            # Passe à 0 les nombres composés
            CouldBePrime[int(vNum/3)::2*uNum] = [0]*int((int(LastNum /6) -int(vNum /6) -1) /uNum +1)
            CouldBePrime[int(wNum/3)::2*uNum] = [0]*int((int(LastNum /6) -int(wNum /6) -1) /uNum +1)
    # Début du renvoi des nombres premiers
    yield 2
    yield 3
    for Num in GetClearedRange(LastNum):
        if CouldBePrime[Num]:
            yield 3 * Num +1 |1

def SequentialPrint(LastNumber, PrimeCount):
    """
    Print the list of prime numbers found by the
    PrimeGenerator function to the console screen.
    """
    for i, j in enumerate(PrimeGenerator(LastNumber)):
        print("{}:{}".format(i + 1, j))
        if i + 1 == PrimeCount:
            break

def ProgramStarter():
    """
    Informs the user of the way to use the program.
    Then ensures that the provided values are correct.
    """
    print("=" * 81,
          "The purpose of this program is to display all primes from 2 to a selected ammount",
          "In order to do that, you must chose 2 real positive numbers",
          "The second one should be less than the first",
          "=" * 81,
          sep='\n'
         )

    LastNumber = input("Limit = ")
    try:
        LastNumber = int(LastNumber)
        assert LastNumber > 0
    except AssertionError:
        print("Incorrect value ! Setting to default : 1 000 000")
        LastNumber = 1000000

    PrimeCount = input("Amount of primes = ")
    try:
        PrimeCount = int(PrimeCount)
        assert PrimeCount > 0 and PrimeCount < LastNumber
    except AssertionError:
        print("Incorrect value ! Setting to default : 10 000")
        PrimeCount = 10000

    return LastNumber, PrimeCount

def Main():
    """
    Launches the program and verify that all options are correctly set.
    """
    LastNumber, PrimeCount = 1000000, 10000 #ProgramStarter()

    while True:
        start = clock()
        SequentialPrint(LastNumber, PrimeCount)
        end = clock()

        print("\nPage générée en", round((end - start), 5), "secondes")
        key = input("Press any key to quit, press return to continue")
        if key != "":
            break

# Début du programme lorsque le fichier est directement appelé uniquement
if __name__ == '__main__':
    Main()
    #input("Press return to continue")
