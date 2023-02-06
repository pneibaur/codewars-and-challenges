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

# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------

"""
Write simple .camelCase method 
(camel_case function in PHP, CamelCase in C# or 
camelCase in Java) for strings. 
All words must have their first letter capitalized 
without spaces.

For instance:

camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord
"""

def camel_case(string):
    #your code here
    return string.title().replace(" ", "")


# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------

"""
Write a function that when given a URL as a string, 
parses out just the domain name and returns it as a string. 
For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
"""

def domain_name(url):
    url = url.replace("https", "").replace("http", "").replace("://", "").replace("www.", "")
    for idx, char in enumerate(url):
        if char == ".":
            url = url[:idx]
    return url

# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------

"""
Move the first letter of each word to the end of it, 
then add "ay" to the end of the word. 
Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

import string
def pig_it(text):
    #your code here
    word_list = text.split(" ")
    latin = "ay"
    for idx, word in enumerate(word_list):
        word_punct = "".join([w for w in word if w in string.punctuation])
        if word in string.punctuation:
            word = word.strip(string.punctuation)
        else:
            if len(word) == 1:
                word = word + latin
            else:
                word = word[1:] + word[0:1] + latin
        word_list[idx] = word + word_punct
    return " ".join(word_list)

# BETTER SOLUTION
def pig_it(text):
    lst = text.split()
    # isalpha() is a funciton that returns true if it's a-z or 0-9
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------

"""
A format for expressing an ordered list of integers 
is to use a comma separated list of either

- individual integers
- or a range of integers denoted by the starting integer 
separated from the end integer in the range by a dash, '-'. 
The range includes all integers in the interval including both endpoints. 
It is not considered a range unless it spans at least 3 numbers. 
For example "12,13,15-17"

Complete the solution so that it takes a list of integers 
in increasing order and returns a correctly formatted string in the range format.

Example:

input([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
"""

def solution(args):
    formatted_str = ""
    for idx, num in enumerate(args):
    #   as long as idx is in range of args...
        if idx < len(args) - 1:
    #       if the num only has bigger nums above (right of) it
            if num + 1 == args[idx + 1] and num - 1 != args[idx - 1]:
                formatted_str += str(num)
    #       if the num only has smaller nums below (left of) it. 
            elif num - 1 == args[idx - 1] and num + 1 != args[idx + 1]:
                if num - 2 != args[idx - 2]:
                    formatted_str += "," + str(num) + ","
                else:
                    formatted_str += "-" + str(num) + ","
    #       if the num does not have any adjacent nums next to it
            elif num - 1 != args[idx - 1] and num + 1 != args[idx + 1]:
                formatted_str += str(num) + ","
            else:
    #           nums in between a run are passed by and not notated. 
                pass
    #   if num is the last in the list...
        else:
            if num - 2 == args[idx - 2]:
                formatted_str += "-" + str(num)
            # check for commas
            else:
                if formatted_str[-1] == ",":
                    formatted_str += str(num)
                else:
                    formatted_str += "," + str(num)
    return(formatted_str)

# BETTER SOLUTION

def solution(args):
    out = []
    # technique to set two variables (beg & end) to args[0]
    beg = end = args[0]
    # technique to start loop on the 2nd number, and then add an empty argument at the end
    # of the 'for' loop. 
    for n in args[1:] + [""]:        
        # this basically controlls three variables: 'beg', 'end', 'n', and sets them at different
        # times in the loop. 
        # 1st time through: beg & end are set to -10 (from input in the description), 
        # while n is set to -9. this doesn't trigger the if statement, so end is now set to 'n', while beg stays the same.
        # once 'n' jumps a few numbers, then it triggers the if statement. 
        if n != end + 1:
            # since end starts increasing right away, this first 'if' is reserved for the 
            # end of the 'for' loop, when everything will be set to the empty argument "".
            if end == beg:
                out.append( str(beg) )
            # if the numbers are adjacent, and the n has jumped some nums. 
            elif end == beg + 1:
                out.extend( [str(beg), str(end)] )
            # since n has jumped nums, and beg and end are different, AND end has been incrementing steadily, 
            # this means it's the end of the run of nums. 
            else:
                out.append( str(beg) + "-" + str(end) )
            # beg gets a new starting num while end continues to increase with n. 
            beg = n
        end = n
    
    return ",".join(out)

# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------

"""
Create a function taking a positive integer between 1 and 3999 (both included) 
as its parameter and returning a string containing the Roman Numeral 
representation of that integer.

Modern Roman numerals are written by expressing each digit 
separately starting with the left most digit and skipping any digit 
with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; 
resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 
1666 uses each Roman symbol in descending order: MDCLXVI.

Example:

solution(1000) # should return 'M'
Remember that there can't be more than 3 identical symbols in a row.

Reference Chart:
Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
"""

def solution(n):
    print(n % 1000)
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    
    k = m[n // 1000]
    bennys = c[(n % 1000) // 100]
    hammys = x[(n % 100) // 10]
    washingtons = i[(n % 10) // 1]
    
    return k + bennys + hammys + washingtons

# BETTER SOLUTION: 

def solution(n):
    # This is great because the key is the number instead of the roman numeral. 
    roman_numerals = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    roman_string = ''
    # start the key at the '1'. 
    for key in sorted(roman_numerals.keys(),reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string