# 1456. Maximum Number of Vowels in a Substring of Given Length. level Medium


"""Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k. Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.


Example 1: 
Input: s = "abciiidef", k = 3 
Output: 3 Explanation: The substring "iii" contains 3 vowel letters. 


Example 2:
Example 1: Input: s = "abciiidef", k = 3 
Output: 3 Explanation: The substring "iii" contains 3 vowel letters. Example 2:


Example 3: 
Input: s = "leetcode", k = 3 
Output: 2 Explanation: "lee", "eet" and "ode" contain 2 vowels."""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        current_count = 0

        # Count vowels in the first window of size k
        for i in range(k):
            if s[i] in vowels:
                current_count += 1
        
        max_count = current_count
        
        # Slide the window from index k to the end
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                current_count -= 1
            if s[i] in vowels:
                current_count += 1
            max_count = max(max_count, current_count)
        
        return max_count
    
print(maxVowels("abciiidef", 3))  # Output: 3
print(maxVowels("aeiou", 2))      # Output: 2
print(maxVowels("leetcode", 3))   # Output: 2    