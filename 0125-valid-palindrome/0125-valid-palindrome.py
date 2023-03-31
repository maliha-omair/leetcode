class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if len(s)<=1:
            return True
        
        letters = "".join(re.split("[^a-zA-Z0-9]*", s.lower()))    
        reverseLetters = letters[::-1]
        print(letters)
        print(reverseLetters)
        if letters == reverseLetters: 
            return True
        else:
            return False
