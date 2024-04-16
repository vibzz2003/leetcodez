class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int size = nums.size();
        if(size==0){
            return 0;
        }
        int i=0;
        int j=1;
        while(j<size){
            if(nums[i]!=nums[j]){
                i+=1;
                nums[i]=nums[j];
            }
            j++;
        }

        size = i+1;

        return size;
        
    }
};