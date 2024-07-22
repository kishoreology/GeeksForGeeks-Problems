#User function Template for python3
class Solution:
    def largestBst(self, root):
        mx=0
        def dfs(cur=root):
            nonlocal mx
            if not cur:
                return False,None,None,None
            if not cur.left and not cur.right:
                mx=max(mx,1)
                return True,cur.data,cur.data,1
            lok,lmn,lmx,lsz=dfs(cur.left)
            rok,rmn,rmx,rsz=dfs(cur.right)
            if lok and rok and lmx<cur.data<rmn:
                mx=max(mx,lsz+1+rsz)
                return True,lmn,rmx,lsz+1+rsz
            if lok and not cur.right and lmx<cur.data:
                mx=max(mx,lsz+1)
                return True,lmn,cur.data,lsz+1
            if not cur.left and rok and cur.data<rmn:
                mx=max(mx,rsz+1)
                return True,cur.data,rmx,rsz+1
            return False,None,None,None
        dfs()
        return mx


#{ 
 # Driver Code Starts
from collections import deque


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == "N":
        return None

    # Creating list of strings from input string after splitting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size += 1

    # Starting from the second element
    i = 1
    while size > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q.popleft()
        size -= 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.left)
            size += 1

        # Move to the next element
        i += 1
        if i >= len(ip):
            break

        currVal = ip[i]

        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.right)
            size += 1

        # Move to the next element
        i += 1

    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)
        ob = Solution()
        result = ob.largestBst(root)
        print(result)

# } Driver Code Ends