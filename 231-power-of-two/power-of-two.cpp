class Solution {
public:
    bool isPowerOfTwo(int n) {
        if(n<0){
            return false;
        }
        return n>0 & not(n & n-1);// 8: 1000 AND (8-1):7: 0111 AND 1000 & 0111 = 0000 ONLY IF N THAT IS 0111 IS A POWER 0F 2 
    }
};