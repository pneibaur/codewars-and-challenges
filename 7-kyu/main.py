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
Write a function that takes an array 
of numbers (integers for the tests) 
and a target number. It should find two different 
items in the array that, when added together, 
give the target value. The indices of these items 
should then be returned in a tuple / list 
(depending on your language) like so: (index1, index2).

For the purposes of this kata, 
some tests may have multiple answers; 
any valid solutions will be accepted.

The input will always be valid 
(numbers will be an array of length 2 or greater, 
and all of the items will be numbers; target will 
always be the sum of two different items from that array).

two_sum([1, 2, 3], 4) # returns [0, 2] or [2, 0]

"""

def two_sum(numbers, target):
    for idx, num in enumerate(numbers):
        slice1 = numbers[:idx]
        slice2 = numbers[(idx + 1):]
        new_list = slice1 + slice2
        diff = target - num
        if diff in new_list:
            diff_idx = numbers.index(diff, idx + 1)
            return [idx, diff_idx]
    return []

# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------

"""
A pangram is a sentence that contains every single letter 
of the alphabet at least once. For example, 
the sentence "The quick brown fox jumps over the lazy dog" 
is a pangram, because it uses the letters A-Z at least once 
(case is irrelevant).

Given a string, detect whether or not it is a pangram. 
Return True if it is, False if not. 
Ignore numbers and punctuation.
"""

def is_pangram(s):
    az_test = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for char in s: 
        if char.lower() in alphabet and char not in az_test: 
            az_test.append(char.lower())
    if len(az_test) == len(alphabet):
        return True
    else: 
        return False