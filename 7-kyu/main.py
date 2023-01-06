"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. 
Additionally, if the number is negative, return 0 (for languages that do have them).

Note: If the number is a multiple of both 3 and 5, only count it once.
"""

from array import array


def solution(number):
    if number < 1: return 0
    num_list = [num for num in range(number) if num % 3 == 0 or num % 5 == 0]
    return sum(num_list)

# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------

"""
Write a function named first_non_repeating_letter 
that takes a string input, and returns the first character 
that is not repeated anywhere in the string.

For example, if given the input 'stress', 
the function should return 't', since the letter t 
only occurs once in the string, and occurs first in the string.

As an added challenge, 
upper- and lowercase letters are considered the same character, 
but the function should return the correct case for the initial 
letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, 
it should return an empty string ("") or 
None -- see sample tests.

"""

def first_non_repeating_letter(string):
    #your code here
    for c in string: 
        if string.lower().count(c.lower()) == 1:
            return c
    return ""


# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------

"""

"""