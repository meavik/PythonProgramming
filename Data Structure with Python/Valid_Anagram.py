def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    freq1, freq2 = {}, {}
    for i in str1:
        if i in freq1:
            freq1[i] += 1
        else:
            freq1[i] = 1
    for j in str2:
        if j in freq2:
            freq2[j] += 1
        else:
            freq2[j] = 1
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
    return True


s1 = input("Enter a word: ")
s2 = input("Enter another word: ")
x = is_anagram(s1, s2)
if x:
    print("Anagram")
else:
    print("Not Anagram")
    
    
####################
####################
####################
from collections import Counter


def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    return Counter(str1) == Counter(str2)


s1 = input("Enter a word: ")
s2 = input("Enter another word: ")
x = is_anagram(s1,s2)
if x:
    print("Anagram")
else:
    print("Not Anagram")
####################
####################
####################
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)
