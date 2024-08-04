class Solution:
    def maximumMeetings(self,n,start,end):
        meetings = sorted(zip(start, end), key=lambda x: x[1])
        count = 1
        last_end_time = meetings[0][1]
        for i in range(1, n):
            current_start_time, current_end_time = meetings[i]
            if current_start_time > last_end_time:
                count += 1
                last_end_time = current_end_time
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends