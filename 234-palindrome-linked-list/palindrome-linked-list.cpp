/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode* temp = head;
        vector<int>data;

        while(temp!=NULL){
            data.push_back(temp->val);
            temp = temp->next;
        }

        int n = data.size();
        int i = 0;
        int j = n-1;

        while(i<=j){
            if(data[i]!=data[j]){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
};