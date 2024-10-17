#User function Template for python3
'''
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def alternatingSplitList(self, head):
        #Your code here
        d1=c1=Node(0)
        d2=c2 = Node(0)
        curr = head
        c = 1
        while curr:
            # print(c)
            # print(curr.data)
            if (c%2!=0):
                c1.next = curr
                c1 = c1.next
                temp1=c1
            else:
                c2.next = curr
                c2 = c2.next
                temp2=c2
         
            c+=1
            curr=curr.next
        temp1.next=None
        temp2.next=None
        return [d1.next,d2.next]


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        head = Node(arr[0])
        tail = head

        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next

        ob = Solution()
        result = ob.alternatingSplitList(head)
        printList(result[0])
        printList(result[1])

# } Driver Code Ends