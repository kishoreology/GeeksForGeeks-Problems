class Solution:
    def findExtra(self,n,a,b):
        sum1=0
        sum2=0
        for i in a:
            sum1=sum1+i
            i+=1
        for j in b:
            sum2=sum2+j
            j+=1
        return(a.index(sum1-sum2))


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(Solution().findExtra(n, a, b))

# } Driver Code Ends