class Solution {
public:
    bool canJump(vector<int>& nums) {
        if(nums.size() == 1) true;
        int jump = 1;
        int i=0;
        while(i < nums.size()-1){
            jump--;
            if(nums[i] == 0 && jump == 0){
                return false;
            }
            jump = max(jump, nums[i]);
            i++;
        }

        return true;
    }
};
