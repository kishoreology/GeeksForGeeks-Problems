 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        ans = 1
        count = 1
        a = set(arr)
        lasta = []
        for i in a:
            lasta.append(i)
        lasta.sort()
        for i in range(1,len(a)):
            
            if lasta[i-1]+1==lasta[i]:
                count +=1
            else:
                ans = max(ans,count)
                count = 1
        # print(lasta)
        ans = max(ans, count) # last check that where you end and else part not run.
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        print(Solution().longestConsecutive(a))
        print("~")
# } Driver Code Ends