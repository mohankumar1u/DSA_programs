class Solution(object):
    def lengthOfLongestSubstring(self, s):
        substrings={}
        max=0
        currentsubstring=""

        for ele in s:
            if(ele in substrings):
                substrings[ele]=ele
                #currentsubstring=ele
                nextsub=""
                for each in currentsubstring.split(str(ele)):
                    nextsub=str(each)
                

                # if 1 in nextsub:
                #     print("nextsub here",nextsub)
                currentsubstring=nextsub+ele
                if max<len(currentsubstring):
                    max=len(currentsubstring)
            else:
                currentsubstring=currentsubstring+ele
                substrings[ele]=ele
                substrings[currentsubstring]=currentsubstring
                if max<len(currentsubstring):
                    max=len(currentsubstring)

        return max
        """
        :type s: str
        :rtype: int
        """
        