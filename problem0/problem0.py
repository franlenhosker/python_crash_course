"""
The FizzBuzz problem.
"""

#############
# FUNCTIONS #
#############

def fizzbuzz():
    """
    Make me function which prints the numbers 1 to 100. HOWEVER, for some
    numbers, I want you to print a word instead of a number.

    If the number is divisible by 3, I want you to print FIZZ.

    If the number is divisible by 5, I want you to print BUZZ.

    HOWEVER, if the number is divisible by BOTH 3 AND 5, I want you to print
    FIZZBUZZ - all on one line - and NOT FIZZ or BUZZ separately.

    Hint (1): Start of by printing the numbers 1 to 100 normally, and then
    sculpt your solution from there.

    Hint (2): Use the REMAINDER operator: %. For example: 13%3 is 1. 12%3 is 2.
    """
    for number in range (1,101):
        if number%3 == 0 and number%5 == 0:
            print ("FIZZBUZZ")
        elif number % 3 == 0:
            print("FIZZ")
        elif number % 5 == 0:
            print ("BUZZ")
        else:
            print(number)

###################
# RUN AND WRAP UP #
###################

def run():
    """ Run this file. """
    fizzbuzz()

if __name__ == "__main__":
    run()
