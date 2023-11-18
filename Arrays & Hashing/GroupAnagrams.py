
#there is some logical eerror in my initial way of trying to solve this (brute force)
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        output = []
        for n in range(len(strs)):
            array = []
            for m in range(len(strs)):
                if sorted(strs[n]) == sorted(strs[m]):
                    array.append(strs[m])
            if array not in output:
                output.append(array)
        return output
    
#need to use dictionaries and tuples soon, more efficient in computing time and complexity