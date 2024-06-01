
class Solution:
    def oddEven(self, s : str) -> str:
        x = y = 0
        count = {}
        temp = set(s)
        for i in s:
            count[i] = count.get(i,0)+1
        for i in temp:
            k = ord(i)-96
            if k%2 == count.get(i) % 2:
                if k & 1:
                    y+=1
                else:
                    x+=1
        return "ODD" if (x+y)&1 else "EVEN"



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.oddEven(s)

        print(res)

# } Driver Code Ends