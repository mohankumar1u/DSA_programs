class Solution(object):
    def threeSum(self, nums):
        result=[]
        nums.sort()
        
        for x in range(len(nums)):
            i=x+1
            j=len(nums)-1
            if(i>=j):
                continue
            while(i<j):
                value=nums[x]+nums[i]+nums[j]
                if(value==0):
                    if([nums[x],nums[i],nums[j]] in result):
                        i+=1
                        continue
                    result.append([nums[x],nums[i],nums[j]])
                    if(i<j and nums[i]==nums[i+1]):
                        i+=1
                    if(i<j and nums[j]==nums[j-1]):
                        j-=1
                    i+=1
                    j-=1
                elif(value>0):
                    j-=1
                elif(value<0):
                    i+=1

        return result
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        