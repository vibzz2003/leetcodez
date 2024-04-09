#include<vector>
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        //base concept : recursion
        //ek baar left to right, then right t left and then so on
        // base case
        vector<vector<int>>result;
        if(root==nullptr) return result;

        queue<TreeNode*>q;
        q.push(root);

        //boolean value telling to go left2right or right2left
        bool left2right = true;

        while(!q.empty()){
            int size = q.size();
            vector<int>ans(size);

            for(int i=0; i<size; i++){
                TreeNode* frontnode = q.front();
                q.pop();

                //if left2right then index is from i else from size-i-1
                int index = left2right ? i : size-i-1;
                ans[index] = frontnode->val;

                if(frontnode->left){
                    q.push(frontnode->left);
                }

                if(frontnode->right){
                    q.push(frontnode->right);
                }

            }

            //changing the direction after every level
            left2right = !left2right;

            result.push_back(ans);

        }
        return result;

    }
};