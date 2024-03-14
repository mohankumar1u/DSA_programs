class Solution(object):
    def romanToInt(self, s):
        romanNumbers={}
        romanNumbers["I"]=1
        romanNumbers["V"]=5
        romanNumbers["X"]=10
        romanNumbers["L"]=50
        romanNumbers["C"]=100
        romanNumbers["D"]=500
        romanNumbers["M"]=1000
        romanNumbers["IV"]=4
        romanNumbers["IX"]=9
        romanNumbers["XL"]=40
        romanNumbers["XC"]=90
        romanNumbers["CD"]=400
        romanNumbers["CM"]=900
        result=0
        i=0
        while(i<len(s)):
            if((i+1)< len(s)and romanNumbers[s[i]]<romanNumbers[s[i+1]]):
                result=result+romanNumbers[s[i]+""+s[i+1]]
                i=i+2
            else:
                result=result+romanNumbers[s[i]]
                i+=1

        return result
        """
        :type s: str
        :rtype: int
        """
        