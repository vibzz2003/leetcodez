class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n==1){
            return nums[0];
        }
        if(n==2){
            return max(nums[0],nums[1]);
        }
       vector<int>money1(n-1);
       money1[0] = nums[0];
       money1[1] = max(nums[1],nums[0]);
       for(int i=2;i<n-1;i++){
            int totalmoney=max(nums[i]+money1[i-2],money1[i-1]);
            money1[i] = totalmoney;
       }
       vector<int>money2(n-1);
       money2[0]= nums[1];
       money2[1] =max(nums[1],nums[2]);
       for(int i=3;i<n;i++){
        money2[i-1]=max(nums[i]+money2[i-2-1],money2[i-1-1]);
       }
       return max(money1[n-2],money2[n-2]);
    }
};