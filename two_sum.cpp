//https://leetcode.com/problems/two-sum/
class Solution {
public:
    bool equalsTarget(int target, int num){
        return(target == num);
    }
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> arr;
        int sum = nums.at(0) + nums.at(1);
        for(int i = 0; i < nums.size(); i++){
            for(int j = 0; j < nums.size(); j++){
                if(i != j){
                    if (equalsTarget(target, nums.at(i) + nums.at(j))){
                        arr.push_back(i);
                        arr.push_back(j);
                        return arr;
                    }
                }
            }
        }
        return arr;
    }
};
