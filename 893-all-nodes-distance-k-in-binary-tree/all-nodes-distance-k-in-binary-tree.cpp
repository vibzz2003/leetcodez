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
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        vector<int>ans;
        unordered_map<TreeNode* , TreeNode*>parent;

        populateMap(root, nullptr, parent);

        unordered_map<TreeNode* , bool>visited;

        queue<TreeNode*>q;
        q.push(target);
        visited[target] = true;
        int level = 0;

        while(!q.empty()){
            int size = q.size();
            for(int i=0; i<size; i++){
                TreeNode* curr = q.front();
                q.pop();
                if(level == k){
                    ans.push_back(curr->val);
                }
                if(curr->left && !visited[curr->left]){
                    q.push(curr->left);
                    visited[curr->left] = true;
                }
                if(curr->right && !visited[curr->right]){
                    q.push(curr->right);
                    visited[curr->right] = true;
                }

                TreeNode* parentNode = parent[curr];
                if(parentNode && !visited[parentNode]){
                    q.push(parentNode);
                    visited[parentNode] = true;
                }
            }
            ++level;
            if(level > k)break;
        }
        return ans;
    }
private:
    void populateMap(TreeNode* node, TreeNode* par, unordered_map<TreeNode*, TreeNode*>&parent){
        if(node==NULL){
            return;
        }

        parent[node] = par;
        populateMap(node->left, node, parent);
        populateMap(node->right, node, parent);
    }
};