class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        if len(t) != len(s):
            return False
        for indx in range (0,len(s)):
            key = s[indx]
            if key in dict.keys():
                dict[key] = dict[key]+1
            else:
                dict[key] = 1 
        
        print ("dict is", dict)
        count = len(dict)
        for indx in range (0,len(t)):
            
            key = t[indx]
            if key in dict.keys():
                dict[key] = dict[key]-1
                if dict[key] <= -1:
                    return False
                count = count - 1 
            else:
                return False
            
        print("values in dict", dict, " count", count)
                
        if count <= 0:
            return True
        else:
            return False
                                  
     