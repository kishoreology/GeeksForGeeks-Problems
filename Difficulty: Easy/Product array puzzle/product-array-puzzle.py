#User function Template for python3

class Solution:
    def productExceptSelf(self, nums):
        #code here
        pro=nums[0]
        zeroes=0
        for i in nums[1:]:
            if i==0:
                zeroes+=1
                continue
            pro*=i
        ans=[]
        if zeroes>1:
            pro=0
        for i in range(len(nums)):
            if nums[i]==0:
                ans.append(pro)
            elif zeroes>=1:
                ans.append(0)
            else:
                
                ans.append(pro//nums[i])
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)

# } Driver Code Ends