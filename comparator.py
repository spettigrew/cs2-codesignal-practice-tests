"""
Comparators are used to compare two objects. In this challenge, you'll create a comparator and use it to sort an array. The Player class is provided in the editor below. It has two fields:

: a string.
: an integer.
Given an array of  Player objects, write a comparator that sorts them in order of decreasing score. If  or more players have the same score, sort those players alphabetically ascending by name. To do this, you must create a Checker class that implements the Comparator interface, then write an int compare(Player a, Player b) method implementing the Comparator.compare(T o1, T o2) method. In short, when sorting in ascending order, a comparator function returns  if ,  if , and  if .

Declare a Checker class that implements the comparator method as described. It should sort first descending by score, then ascending by name. The code stub reads the input, creates a list of Player objects, uses your method to sort the data, and prints it out properly.

Example
 

Sort the list as . Sort first descending by score, then ascending by name.

Input Format

The first line contains an integer, , the number of players.
Each of the next  lines contains a player's  and , a string and an integer.

Constraints

Two or more players can have the same name.
Player names consist of lowercase English alphabetic letters.
Output Format

You are not responsible for printing any output to stdout. Locked stub code in Solution will instantiate a Checker object, use it to sort the Player array, and print each sorted element.

Sample Input

5
amy 100
david 100
heraldo 50
aakansha 75
aleksa 150
Sample Output

aleksa 150
amy 100
david 100
aakansha 75
heraldo 50
Explanation

The players are first sorted descending by score, then ascending by name.
"""

from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return f"{self.name} {self.score}"
        
    def comparator(self, a, b):
        if a.score > b.score: # scores decreasing
            return -1
        elif a.score < b.score:
            return 1
        
        if a.name > b.name: # names ascending
            return 1
        elif a.name < b.name:
            return -1
        return 0 


# we are sorting n(log n)
# our implemented item is n, so n(log n), with no comparator
n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

# space is based on inputs, we don't really have a specific input, we don't create variables
# comparator is O(1)
# for this we have a data structure to store data, so in theory it is O(n), but it is our input data

# space is how it changes based on input, but we don't take space into account here
# if input is array, if we don't create anything new for it, the space complexity is O(1)
    
data = sorted(data, key=cmp_to_key(Player.comparator)) # we sorted here
for i in data:
    print(i.name, i.score)