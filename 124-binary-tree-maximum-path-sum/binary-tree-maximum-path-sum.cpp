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
    int maxPathSum(TreeNode* root) {
        //base case
        if(root==NULL){
            return 0;
        }

        int maxsum = INT_MIN;
        maxpathsumhelp(root, maxsum);
        return maxsum;
    }
private:
    int maxpathsumhelp(TreeNode* node, int &maxsum){
        if(node==NULL){
            return 0;
        }

        int leftsum = max(0, maxpathsumhelp(node->left, maxsum));
        int rightsum = max(0, maxpathsumhelp(node->right, maxsum));

        int sumvalue = node->val + leftsum + rightsum;

        maxsum = max(maxsum, sumvalue);

        return node->val + max(leftsum, rightsum);
    }
};