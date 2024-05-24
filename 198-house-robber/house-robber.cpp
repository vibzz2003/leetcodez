class Solution {
public:
    int rob(vector<int>& nums) {
       int n = nums.size();
        if (n==1){
            return nums[0];
        }
       vector<int>money(n);
       money[0] = nums[0];
       money[1] = max(nums[1],nums[0]);
       for(int i=2;i<n;i++){
            int totalmoney=max(nums[i]+money[i-2],money[i-1]);
            money[i] = totalmoney;
       }   
       return money[n-1];
    }
};