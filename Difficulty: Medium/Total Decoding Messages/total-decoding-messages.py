#User function Template for python3
class Solution:
	def countWays(self, digits):
		# Code here
		from functools import lru_cache
        @lru_cache(None)
        def dfs(ix=len(digits)-1):
            nonlocal digits
            if ix<0:
                return 1
            ret=0
            if 1<=int(digits[ix])<=9:
                ret+=dfs(ix-1)
            if ix-1>=0 and 10<=int(digits[ix-1]+digits[ix])<=26:
                ret+=dfs(ix-2)
            return ret
        return dfs()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        digits = input()
        ob = Solution()
        ans = ob.countWays(digits)
        print(ans)
        print("~")

# } Driver Code Ends