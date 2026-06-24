class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int hold = 0x0;
        for (int num : nums){
            hold = hold ^ num;
        }
        return hold;
    }
};
