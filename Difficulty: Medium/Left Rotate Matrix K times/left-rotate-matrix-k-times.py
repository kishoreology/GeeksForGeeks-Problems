class Solution:
    def rotateMatrix(self, k, mat):
        new_mat = []
        temp_k = k%len(mat[0])
        
        if (temp_k == 0):
            return mat
        else:
            for sub in mat:
                new_mat.append(sub[temp_k:]+sub[:temp_k])
        
        return new_mat



#{ 
 # Driver Code Starts
import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().strip().split(" "))
        mat = []
        for i in range(n):
            mat.append(list(map(int, input().strip().split(" "))))
        ob = Solution()
        ans = ob.rotateMatrix(k, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end=" ")
            print()

# } Driver Code Ends