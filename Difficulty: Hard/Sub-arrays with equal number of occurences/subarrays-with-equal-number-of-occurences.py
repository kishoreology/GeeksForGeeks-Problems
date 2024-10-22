#User function Template for python3

class Solution:
    def sameOccurrence(self, arr, x, y):
        # code here
        d = {}
        pre = 0
        res= 0
        for i in range(len(arr)):
            if arr[i]==x:
                pre+=x 
            if arr[i]==y:
                pre+= -x 
            if pre==0:
                res+=1
                
            if pre in d:
                res+= d[pre]
            d[pre] = d.get(pre,0)+1
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        x = int(input().strip())
        y = int(input().strip())
        ob = Solution()
        ans = ob.sameOccurrence(arr, x, y)
        print(ans)
        tc -= 1

# } Driver Code Ends