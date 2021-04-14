//https://leetcode.com/submissions/detail/452604804/
class Solution {
public:

    int searchInsert(vector<int>& nums, int target) {
        int midVal = (nums.size()  - 1) / 2, high = nums.size() - 1 , low = 0, index = 0;
        if (target < nums[0]) return 0;
        else{
            if(target > nums[high] ) return high + 1;
        }
        while ( low <= high ){
            if(nums[midVal] == target){
                return midVal;
            } else{
                if (nums[midVal] < target){
                    low = midVal + 1;
                    midVal = (high + low) /2 ;

                } else{
                    high = midVal - 1;
                    midVal = (high + low) /2 ;
                }
            }
        }
        if(nums[low - 1 ]< target && target > nums[high] ){
            return low;
        }
        return index;
    }
};
