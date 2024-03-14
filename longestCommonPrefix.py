class Solution(object):
    def longestCommonPrefix(self, strs):
        LCP=""
        for each in strs[0]:
            for i in range(1,len(strs)):
                index=len(LCP)
                if(index>=len(strs[i])):
                    return LCP
                if(each!=strs[i][index]):
                    return LCP
            LCP=LCP+each
        return LCP

        """
        :type strs: List[str]
        :rtype: str
        """
        