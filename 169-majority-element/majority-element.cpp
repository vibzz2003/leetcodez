class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();
        map<int, int>new_map;
        for(int i=0; i<n; i++){
            new_map[nums[i]]++; //new_map[nums[i]]++;
        }

        int majorityelement = -1;
        int maxcount = n/2;

        for(const auto& pair : new_map){ //for(const auto& pair : new_map)
            if(pair.second>maxcount){
                maxcount=pair.second; 
                majorityelement = pair.first;
            }
        }

        return majorityelement;
    }
};