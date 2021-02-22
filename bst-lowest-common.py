"""
You are given pointer to the root of the binary search tree and two values v1 and v2. You need to return the lowest common ancestor (LCA) of v1 and v2 in the binary search tree.

                    2
                    /\
                   1  3
                     / \
                    4   5
                        |
                        6                      

In the diagram above, the lowest common ancestor of the nodes 4 and 6 is the node 3. Node 3 is the lowest node which has nodes 4 and 6 as descendants.

Function Description

Complete the function lca in the editor below. It should return a pointer to the lowest common ancestor node of the two values given.

lca has the following parameters:
- root: a pointer to the root node of a binary search tree
- v1: a node.data value
- v2: a node.data value

Input Format

The first line contains an integer, n, the number of nodes in the tree.
The second line contains n space-separated integers representing node.data values.
The third line contains two space-separated integers, v1 and v2.

To use the test data, you will have to create the binary search tree yourself. Here on the platform, the tree will be created for you.

Constraints
1 <= n, node.data <= 25
1 <= v1, v2 <= 25
v1 != v2

The tree will contain nodes with data equal to v1 and v2.

Output Format

Return the a pointer to the node that is the lowest common ancestor of v1 and v2.

Sample Input

6
4 2 3 1 7 6
1 7

image
                    4
                   / \ 
                  2   7
                 / \ /
                1  3 6

 v1 = 1 and v2 = 7.

Sample Output

[reference to node 4]

Explanation

LCA of 1 and 7 is 4, the root in this case.
Return a pointer to the node.
"""

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
"""

def lca(root, v1, v2):      # Big O  = O(n)
  #Enter your code here - LCA = lowest common ancestor
    # base case:

    # three different options:          

    # LCA is to the left
        #compare the value of the root to v1 and v2
        # v1 and v2 ar less than root.info
        # recurse left
        if root.info > v1 and root.info > v2:
            lca(root.left, v1, v2)
    # LCA is to the right
        # v1 and v2 are greater than root
        # recurse right
        elif root.info < v1 and root.info < v2:
            lca(root.right, v1, v2)
    # LCA is the node
        # root is split between v1 and v2
        else:
            return root



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)