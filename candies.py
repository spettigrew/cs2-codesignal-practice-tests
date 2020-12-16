"""
n children have got m pieces of candy. They want to eat as much candy as they can, but each child must eat exactly the same amount of candy as any other child. Determine how many pieces of candy will be eaten by all the children together. Individual pieces of candy cannot be split.

Example

For n = 3 and m = 10, the output should be
candies(n, m) = 9.

Each child will eat 3 pieces. So the answer is 9.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

The number of children.

Guaranteed constraints:
1 ≤ n ≤ 10.

[input] integer m

The number of pieces of candy.

Guaranteed constraints:
2 ≤ m ≤ 100.

[output] integer

The total number of pieces of candy the children will eat provided they eat as much as they can and all children eat the same amount.
"""

def candies(n, m):
    # kids should get equal amounts of candy. No more than 10 kids, no more than 100 pieces of candy

    # get number of children, hard divide by pieces of candy
    # return pieces of candy for each child times each one to get the equal amount of candy
    # print(m // n)
    return (m // n) * n
    
    # candy = (m // n)
    # results = candy * n 
    # return result 
    
    # children = n
    # candy = m
  
    # candy_divide = children // candy
    # individual_child_share = candy_divide * children
    # return individual_child_share