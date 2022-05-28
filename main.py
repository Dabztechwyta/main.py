# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

s1 = input("enter your first word: ")
s2 = input("enter your second word: ")

def find_anagrams(word):
    # [assignment] Add your code here
    if sorted(s1) == sorted(s2):
        print("this is an anagram")
        return True
    else:
        print("this is not an anagram")
        return False
    
print(find_anagrams(s1))

