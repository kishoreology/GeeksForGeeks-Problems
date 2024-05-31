#User function Template for python3
class Solution:
    def swapNibbles (self, n):
        bi = bin(n)[2:].zfill(8)
        swap = bi[4:] + bi[:4]
        return int(swap, 2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        print(ob.swapNibbles(n))

# } Driver Code Ends