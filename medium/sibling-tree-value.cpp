#include "solution.hpp"
using namespace std;

/**
 * class Tree {
 *     public:
 *         int val;
 *         Tree *left;
 *         Tree *right;
 * };
 */
class Solution {
    public:
    int solve(Tree* root, int k) {
        // Write your code here
        Tree *prev;
        while (root) {
            if (root->val < k) {
                prev = root;
                root = root->right;
            }
            else if (root->val > k) {
                prev = root;
                root = root->left;
            }
            else {
                break;
            }
        }
        return prev->right->val == k ? prev->left->val : prev->right->val;
    }
};
