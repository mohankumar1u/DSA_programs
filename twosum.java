class Solution {
    public int[] twoSum(int[] nums, int target) {
        int index=0;
        int pointer=1;
        int n=nums.length;
        boolean foundResult=false;
        int[] result={-1,-1};
        while(index<n){

            while(pointer<n){
                if(nums[index]+nums[pointer] == target){
                    result[0]=index;
                    result[1]=pointer;
                    return result;
                }
                pointer=pointer+1;
            }

            index=index+1;
            pointer=index+1;
        }
        return result;
    }
}