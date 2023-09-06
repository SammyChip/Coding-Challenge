class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
    #   Hashmap method
        if len(s) != len(t): #early exit
            return False
 
        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1+ countS.get(s[i],0)
            countT[s[i]] = 1+ countT.get(t[i],0)

        for j in countS:
            if countS[j] != countT.get(j,0):
                return False
        return True
    
    #or use return Counter(s) == Counter(t) or #return sorted(s) ==  sorted(t)
            
