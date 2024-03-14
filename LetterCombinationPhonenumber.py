class Solution(object):
    def letterCombinations(self, digits):
        result=[]
        if(digits==""):
            return result
        numberMap={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        
        def genarateCode(currentString, reminingDigits):
            if(reminingDigits==""):
                    result.append(currentString)
                    return 0
            for each in numberMap[reminingDigits[0]]:
                genarateCode(currentString+each,reminingDigits[1:])
        genarateCode("", digits)
        return result
        """
        :type digits: str
        :rtype: List[str]
        """
        