#User function Template for python3

class Solution:
    #Complete this function
    #Function to find the maximum occurred integer in all ranges.
    def maxOccured(self,n, l, r, maxx):
        dp = [0]*(maxx+2)
        count = 0
        ans = -1
        curr = 0
        for i in range(n):
            dp[l[i]] += 1
            dp[r[i]+1] -= 1
        for i in range(1, maxx + 1):
            curr += dp[i]
            if curr > count:
                ans = i
                count = curr
        return ans 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

A = [0] * 1000000


def main():

    T = int(input())

    while (T > 0):

        global A
        A = [0] * 1000000

        n = int(input())

        l = [int(x) for x in input().strip().split()]
        r = [int(x) for x in input().strip().split()]

        maxx = max(r)
        ob = Solution()
        print(ob.maxOccured(n, l, r, maxx))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends