"""2573. Find the String with LCP
We define the lcp matrix of any 0-indexed string word of n lowercase English letters as an n x n grid such that:
lcp[i][j] is equal to the length of the longest common prefix between the substrings word[i,n-1] and word[j,n-1].
Given an n x n matrix lcp, return the alphabetically smallest string word that corresponds to lcp. If there is no such string, return an empty string.
A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b. For example, "aabd" is lexicographically smaller than "aaca" because the first position they differ is at the third letter, and 'b' comes before 'c'.


Example 1:
Input: lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
Output: "abab"
Explanation: lcp corresponds to any 4 letter string with two alternating letters. The lexicographically smallest of them is "abab".


Example 2:
Input: lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
Output: "aaaa"
Explanation: lcp corresponds to any 4 letter string with a single distinct letter. The lexicographically smallest of them is "aaaa". 


Example 3:
Input: lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]
Output: ""
Explanation: lcp[3][3] cannot be equal to 3 since word[3,...,3] consists of only a single letter; Thus, no answer exists.
 """
 
 
from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)

        # Step 1: basic validation
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""

        # DSU (Union-Find)
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        # Step 2: union positions with lcp[i][j] > 0
        for i in range(n):
            for j in range(n):
                if lcp[i][j] > 0:
                    union(i, j)

        # Step 3: assign characters
        group_to_char = {}
        res = [''] * n
        cur_char = 0

        for i in range(n):
            root = find(i)
            if root not in group_to_char:
                if cur_char >= 26:
                    return ""
                group_to_char[root] = chr(ord('a') + cur_char)
                cur_char += 1
            res[i] = group_to_char[root]

        word = "".join(res)

        # Step 4: validate by recomputing LCP
        dp = [[0]*n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word[i] == word[j]:
                    if i+1 < n and j+1 < n:
                        dp[i][j] = 1 + dp[i+1][j+1]
                    else:
                        dp[i][j] = 1
                else:
                    dp[i][j] = 0

                if dp[i][j] != lcp[i][j]:
                    return ""

        return word


