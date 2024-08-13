#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, n): 
        #Your code here
        l,h=0,n-1
        ans=None
        while l<=h:
            mid=(l+h)//2
            if mid*mid>n:
                h=mid-1
            elif mid*mid<n:
                l=mid+1
                ans=mid
            else:
                return mid
        return ans if n!=1 else 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        x = int(input())

        print(Solution().floorSqrt(x))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends