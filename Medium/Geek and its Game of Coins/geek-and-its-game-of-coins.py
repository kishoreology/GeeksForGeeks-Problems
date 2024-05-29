
class Solution:
    def findWinner(self, n : int, x : int, y : int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            if i - 1 >= 0 and not dp[i - 1]:
                dp[i] = 1
            elif i - x >= 0 and not dp[i - x]:
                dp[i] = 1
            elif i - y >= 0 and not dp[i - y]:
                dp[i] = 1
    
        return 1 if dp[n] else 0
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        x = int(input())

        y = int(input())

        obj = Solution()
        res = obj.findWinner(n, x, y)

        print(res)

# } Driver Code Ends