class Solution:
    def findMaxDiff(self, arr):
        # code here
        stk1 = []
        n = len(arr)
        lsmall = []
        for i in range(n):
            while(len(stk1) and arr[stk1[-1]] >= arr[i]):
                stk1.pop()
            if(not len(stk1)):
                lsmall.append(0)
            else:
                lsmall.append(arr[stk1[-1]])
            stk1.append(i)
        #print(lsmall)
        stk = []
        rsmall = []
        for i in range(n-1,-1,-1):
            while(stk and arr[stk[-1]] >= arr[i]):
                stk.pop()
            if(not stk):
                rsmall.append(0)
            else:
                rsmall.append(arr[stk[-1]])
            stk.append(i)
        rsmall = rsmall[::-1]
        ans = -2**32
        for i in range(n):
            ans = max(ans, abs(lsmall[i]-rsmall[i]))
        #print(rsmall)
        return ans


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.findMaxDiff(arr))

# } Driver Code Ends