# Enumeration
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        length = len(s)
        max_len, result = 0, ""
        
        for center in range(length):
            # Odd case
            start, end = center, center
            while self.valid(start, end, length):
                if s[start] != s[end]:
                    break
                new_len = end - start + 1
                if new_len > max_len:
                    max_len = new_len
                    result = s[start : end + 1]
                start -= 1
                end += 1
            
            # Even case
            start, end = center, center + 1
            while self.valid(start, end, length):
                if s[start] != s[end]:
                    break
                new_len = end - start + 1
                if new_len > max_len:
                    max_len = new_len
                    result = s[start : end + 1]
                start -= 1
                end += 1
        return result
    
    def valid(self, start, end, length):
        return start > -1 and end < length
 
# DP solution
class Solutiondp:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        if not s:
            return ""
            
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        
        for i in range(n):
            is_palindrome[i][i] = True
        for i in range(1, n):
            is_palindrome[i][i - 1] = True
            
        longest, start, end = 1, 0, 0
        for length in range(1, n):
            for i in range(n - length):
                j = i + length
                is_palindrome[i][j] = s[i] == s[j] and is_palindrome[i + 1][j - 1]
                if is_palindrome[i][j] and length + 1 > longest:
                    longest = length + 1
                    start, end = i, j
                    
        return s[start:end + 1]

s=Solution() 
# Solutiondp()
t="abdxdbaz"
print("\nlongest palindrome substring of ", t, "is\n")
print(s.longestPalindrome(t))
