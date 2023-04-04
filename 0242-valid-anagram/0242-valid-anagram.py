class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        for indx in range (0,len(s)):
            t = t.replace(s[indx],'',1)
            # key = s[indx]
            # if key in dict.keys():
            #     dict[key] = dict[key]+1
            # else:
                # dict[key] = 0 
        print("t is", t)
        if t: 
            return False
        else: 
            return True
        # print ("dict is", dict)
        