# Given a string "s". You have to find the longest palindromic substring.You may assume the maximum length of the string is 1000.
# Input: "adda"   Output: "adda"
# Input: "babad"  Output: "baba"
# Input:  "c"     Output: "c"

class Solution:
    def longestPalindrome(self, s:str) -> str:
        def helper(l,r):
            while l>=0 and r<len(s) and s[l] == s[r]:
                l,r=l-1,r+1
            return s[l+1:r]
        res = ''
        for i in range(len(s)):
            odd = helper(i,i)
            even = helper(i,i+1)
            res = max(odd,even,res,key=len)
        return res

ob = Solution()
print(ob.longestPalindrome("baddad"))
print(ob.longestPalindrome("abba"))
print(ob.longestPalindrome("abcdefgh"))
