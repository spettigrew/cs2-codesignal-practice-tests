"""
Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

Example

For year = 1905, the output should be
centuryFromYear(year) = 20;
For year = 1700, the output should be
centuryFromYear(year) = 17.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer year

A positive integer, designating the year.

Guaranteed constraints:
1 ≤ year ≤ 2005.

[output] integer

The number of the century the year is in.
"""

def centuryFromYear(year):
    return (year + 99) // 100

# ------------ Alternative code ---------------------->>>>>>
# year_string = str(year)
# last_two_digits = year_string[len(year_string) -2:]
# # print(last_two_digits)
# # if the integer version of the last two digits is > 0, return the first two numbers (if/else)       or return + 1, else: == 0 return the first num
# if year < 101:
#     return 1
# add_one = False
# if int(last_two_digits) > 0:
#     add_one = True
# if len(year_string) == 4:
#     if add_one == True:
#         return int(year_string[:2]) + 1
#     else:
#         return int(year_string[:2])
# elif len(year_string) == 3:
#     if add_one == True:
#         return int(year_string[:1]) + 1
#     else:
#         return int(year_string[:1])
            