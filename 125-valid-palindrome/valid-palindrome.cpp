class Solution {
public:
    bool isPalindrome(string s) {
        string s1;
        for(char c : s){
            if(isalnum(c)){
                s1 += tolower(c);
            }
        }
        int left=0; 
        int right=s1.length()-1;
        while(left<right){
            if(s1[left]!=s1[right]){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};