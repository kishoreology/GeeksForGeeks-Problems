#User function Template for python3

class Solution:
    def Maximize(self, arr): 
        # Complete the function
        temp = sorted(arr)
        idx = 0
        sum1 = 0
        for i in temp:
            sum1 = sum1 + (i*idx)
            idx +=1
        return sum1%(10**9 + 7)
      



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        # k = int(input())
        ob = Solution()
        print(ob.Maximize(A))

# } Driver Code Ends