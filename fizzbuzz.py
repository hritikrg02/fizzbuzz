"""
file: fizzbuzz.py
description: plays the game of FizzBuzz
language: python3
author: Hritik "Ricky" Gupta
"""

def fizzbuzz():
    """
    prints out the numbers 1 to 100, writing Fizz whenever there's a multiple of 3, and Buzz when there's a multiple of 5
    """
    for i in range(1, 101):
        output = ''
        if i % 3 == 0:
            output += 'Fizz'
        if i % 5 == 0:
            output += 'Buzz'
        if output == '':
            output += str(i)
        print(output)

if __name__ == '__main__':
    fizzbuzz()
