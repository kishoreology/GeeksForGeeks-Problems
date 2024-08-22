#User function Template for python3

from typing import List
from collections import deque, defaultdict

class Solution:
    def findOrder(self, dict: List[str], n: int, k: int) -> str:
        # Your implementation here
        # Step 1: Build the graph
        graph = defaultdict(set)
        in_degree = defaultdict(int)
        all_chars = set()
        
        # Initialize the graph and in-degrees
        for word in dict:
            for char in word:
                if char not in in_degree:
                    in_degree[char] = 0
                all_chars.add(char)
        
        # Create edges between characters based on the dictionary order
        for i in range(len(dict) - 1):
            w1, w2 = dict[i], dict[i+1]
            min_length = min(len(w1), len(w2))
            
            # Find the first differing character
            for j in range(min_length):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break
        
        # Step 2: Perform topological sort using Kahn’s Algorithm
        queue = deque([char for char in all_chars if in_degree[char] == 0])
        order = []
        
        while queue:
            char = queue.popleft()
            order.append(char)
            
            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check if we got a valid topological sort
        if len(order) != len(all_chars):
            return ""  # Cycle detected or not all characters included
        
        return ''.join(order)




#{ 
 # Driver Code Starts
#Initial Template for Python 3


class sort_by_order:

    def __init__(self, s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i

    def transform(self, word):
        new_word = ''
        for c in word:
            new_word += chr(ord('a') + self.priority[c])
        return new_word

    def sort_this_list(self, lst):
        lst.sort(key=self.transform)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        n = int(line[0])
        k = int(line[1])

        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob = Solution()
        order = ob.findOrder(alien_dict, n, k)
        s = ""
        for i in range(k):
            s += chr(97 + i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)

            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)

# } Driver Code Ends