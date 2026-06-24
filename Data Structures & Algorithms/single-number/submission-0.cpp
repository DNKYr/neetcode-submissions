class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int hold = 0x0;
        for (auto num : nums){
            hold = hold ^ num;
        }
        return hold;
    }
};
