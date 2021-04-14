//https://leetcode.com/problems/max-consecutive-ones/submissions/
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int cont = 0;
        int tempCont = 0;
        for (int i = 0; i < nums.size(); i++){
            if(nums.at(i) == 1){
                tempCont++;
                
                if(tempCont > cont){
                    cont = tempCont;
                }
            }
            else{
                tempCont = 0;
            }
        }
        return cont;        
    }
};
