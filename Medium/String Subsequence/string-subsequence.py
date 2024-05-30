
from functools import lru_cache
class Solution:
    def countWays(self, s1 : str, s2 : str) -> int:
        # code here
        n,m,MOD=len(s1),len(s2),1000000007
        
        pre=[0]*(m+1)
        pre[m]=1
        for i in range(n-1,-1,-1):
            curr=[0]*(m+1)
            curr[m]=1
            for j in range(m-1,-1,-1):
                ans=pre[j]%MOD
                if s1[i]==s2[j]:
                    ans+=pre[j+1]%MOD
                curr[j]=ans%MOD
            pre=[k for k in curr]
        return curr[0]%MOD


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s1 = (input())

        s2 = (input())

        obj = Solution()
        res = obj.countWays(s1, s2)

        print(res)

# } Driver Code Ends