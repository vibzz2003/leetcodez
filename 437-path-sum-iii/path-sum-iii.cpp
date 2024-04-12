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
private:
    void solve(TreeNode* root, int targetsum, long sum){
        if(root==nullptr){
            return;
        }

        sum += root->val;
        if(sum == targetsum){
            count++;
        }

        solve(root->left, targetsum, sum);
        solve(root->right, targetsum, sum);
    }
public:
    int count = 0;
    int pathSum(TreeNode* root, int targetSum) {
        //base case
        if(root==nullptr){
            return 0;
        }
        solve(root, targetSum, 0);
        pathSum(root->left, targetSum);
        pathSum(root->right, targetSum);

        return count;
    }
};