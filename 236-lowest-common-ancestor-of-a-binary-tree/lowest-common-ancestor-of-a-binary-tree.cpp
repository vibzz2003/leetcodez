/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* ishelp(TreeNode* root, TreeNode* p, TreeNode* q){
        if(root == NULL || root == p || root == q) return root;

        TreeNode* left = ishelp(root->left, p, q);
        TreeNode* right = ishelp(root->right, p, q);

        if(left == nullptr && right == nullptr){
            return nullptr;
        }
        if(left == nullptr){
            return right;
        }
        if(right == nullptr){
            return left;
        }
        return root;
    }

    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root == nullptr) return nullptr;
        return ishelp(root, p, q);
    }
};
