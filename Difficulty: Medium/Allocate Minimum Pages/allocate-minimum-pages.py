class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        def is_valid(arr, n, k, max_pages):
            students = 1  # Start with one student
            current_pages = 0  # Track current page allocation for a student
            
            # Iterate through all books
            for pages in arr:
                if pages > max_pages:
                    return False  # If a single book has more pages than max_pages, allocation is not possible
                if current_pages + pages > max_pages:
                    students += 1  # Allocate to a new student
                    current_pages = pages  # Start new allocation with current book
                    if students > k:
                        return False  # If students exceed k, allocation is not valid
                else:
                    current_pages += pages  # Add book pages to current student's allocation
            
            return True  # Allocation is valid within the constraints
        
        n = len(arr)  # Total number of books
        if k > n:
            return -1  # If students exceed books, allocation is not possible
        
        low = max(arr)  # Minimum pages to allocate (at least one book with max pages)
        high = sum(arr)  # Maximum pages to allocate (all books to one student)
        result = -1  # Variable to store the result
        
        # Binary search to find the minimum maximum pages
        while low <= high:
            mid = (low + high) // 2  # Midpoint of the current range
            if is_valid(arr, n, k, mid):
                result = mid  # Update result with the current valid allocation
                high = mid - 1  # Try for a smaller maximum by reducing the range
            else:
                low = mid + 1  # Increase the range for a valid allocation
        
        return result  # Return the minimum of the maximum pages



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.findPages(A, D)
        print(ans)
        print("~")

# } Driver Code Ends