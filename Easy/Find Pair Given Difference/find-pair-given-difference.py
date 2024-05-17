
from typing import List


class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        arr.sort()
        i, j = 0, 1
        while j < len(arr):
            if arr[j] - arr[i] == x:
                return 1
            elif arr[j] - arr[i] < x:
                j += 1
            elif arr[j] - arr[i] > x:
                i += 1
                if i==j:
                    j+=1
        return -1
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        x = int(input())

        arr = IntArray().Input(n)

        obj = Solution()
        res = obj.findPair(n, x, arr)

        print(res)

# } Driver Code Ends