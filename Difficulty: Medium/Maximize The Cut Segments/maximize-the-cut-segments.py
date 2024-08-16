#User function Template for python3


class Solution:
    def maximizeTheCuts(self, total_length, cut_length_x, cut_length_y, cut_length_z):
        # Initialize a DP array where dp[i] stores the maximum number of cuts for length i
        dp = [0] + [float("-inf")] * total_length
       
        # Iterate through each length from 1 to total_length
        for current_length in range(1, total_length + 1):
            # If current_length is greater than or equal to cut_length_x, consider cutting it
            max_cuts_x = 1 + dp[current_length - cut_length_x] if current_length >= cut_length_x else dp[current_length]
           
            # If current_length is greater than or equal to cut_length_y, consider cutting it
            max_cuts_y = 1 + dp[current_length - cut_length_y] if current_length >= cut_length_y else dp[current_length]
           
            # If current_length is greater than or equal to cut_length_z, consider cutting it
            max_cuts_z = 1 + dp[current_length - cut_length_z] if current_length >= cut_length_z else dp[current_length]
           
            # Update dp[current_length] with the maximum cuts possible
            dp[current_length] = max(dp[current_length], max_cuts_x, max_cuts_y, max_cuts_z)

        # The result is the maximum number of cuts possible for total_length
        # Return 0 if no cuts can be made (i.e., result is negative)
        return max(0, dp[-1])

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        x,y,z=[int(x) for x in input().split()]
        
        print(Solution().maximizeTheCuts(n,x,y,z))
# } Driver Code Ends