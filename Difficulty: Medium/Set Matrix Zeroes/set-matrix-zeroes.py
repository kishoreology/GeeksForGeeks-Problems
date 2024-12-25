#User function Template for python3
class Solution:
    def setMatrixZeroes(self, mat):
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                if mat[i][j] == 0:
                    # Mark the entire row and column with None
                    for k in range(len(mat)):
                        if mat[k][j] != 0:
                            mat[k][j] = None
                    for k in range(len(mat[0])):
                        if mat[i][k] != 0:
                            mat[i][k] = None
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                if mat[i][j] is None:
                    mat[i][j] = 0
        
        return mat

#{ 
 # Driver Code Starts
import sys

# Position this line where user code will be pasted.
if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()

    idx = 0
    t = int(data[idx])
    idx += 1
    results = []

    for _ in range(t):
        n, m = map(int, data[idx:idx + 2])
        idx += 2
        arr = []
        for i in range(n):
            arr.append(list(map(int, data[idx:idx + m])))
            idx += m

        sol = Solution()
        sol.setMatrixZeroes(arr)

        for row in arr:
            results.append(" ".join(map(str, row)))

        results.append("~")

    sys.stdout.write("\n".join(results) + "\n")

# } Driver Code Ends