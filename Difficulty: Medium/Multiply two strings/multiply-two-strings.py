#User function Template for python3

class Solution:
    def multiplyStrings(self, s1, s2):
        # code here
        # return the product string
        def multiply(s, d):
            n = len(s)
            carry, r = 0, 0
            m = 1
            d = ord(d) - ord('0')
            #for i in range(n-1, -1, -1):
            i = n-1
            while i >= 0 or carry > 0:
                p = 0
                if i >= 0:
                    p += (ord(s[i])-ord('0'))*d
                p += carry
                r += (p%10)*m 
                
                carry = p//10
                m *= 10
                i -= 1
            
            return r
            
        sign = 1
        match (s1[0], s2[0]):
            case ('-', '-'):
                s1 = s1[1:]
                s2 = s2[1:]
            case ('-', _):
                s1 = s1[1:]
                sign = -1
            case (_, '-'):
                s2 = s2[1:]
                sign = -1
            case (_, _):
                pass
            
        n = len(s2)
        m = 1
        ans = 0
        for i in range(n-1, -1, -1):
            ans += multiply(s1, s2[i]) * m
            m *= 10
        return ans*sign


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a = input()
        b = input()
        print(Solution().multiplyStrings(a.strip(), b.strip()))

        print("~")

# } Driver Code Ends