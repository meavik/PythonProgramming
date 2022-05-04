# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Input:"A man, a plan, a canal: Panama"
# Output: True
# Input: "Race a car"
# Output:False
~~~~~~~~~~~~~~~~~~~~~~~~~~
# using library functions
~~~~~~~~~~~~~~~~~~~~~~~~~~
# class Solution:
#     def validPalindrome(self, s:str)->bool:
#         newStr = ""
#         for c in s:
#             if c.isalnum():
#                 newStr += c.lower()
#         return newStr == newStr[::-1]


class Solution:
    def alphaNum(self, c):
        return (
            ord('A')<= ord(c) <= ord('Z') or
            ord('a')<= ord(c) <= ord ('z') or
            ord('0') <=ord(c) <= ord('9')
        )
    
    def validPalindrome(self, s:str)->bool:
        l,r = 0,len(s)-1
        while l<r:
            while l<r and not self.alphaNum(s[l]):
                l += 1
            while r>l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1,r-1
        return True

obj = Solution()
print(obj.validPalindrome('A man, a plan, a canal: Panama'))
print(obj.validPalindrome("raceacar"))
print(obj.validPalindrome('111'))
