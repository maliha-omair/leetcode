class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i]== "[":
                arr.append(s[i])
            else:
                if len(arr)==0:
                    return False
                char = arr.pop()
                if s[i] == ")" and char != "(":
                    return False
                if s[i] == "]" and char != "[":
                    return False
                if s[i] == "}" and char != "{":
                    return False
                
        return len(arr)==0 
                
                                
                