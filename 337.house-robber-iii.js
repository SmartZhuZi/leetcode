/*
 * @lc app=leetcode id=337 lang=javascript
 *
 * [337] House Robber III
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var rob = function(root) {

    temp = travelsal(root);
    return Math.max(temp[0],temp[1]);
};

const travelsal = (node) => {
    if (node === null){
        return [0,0];
    }
    const left = travelsal(node.left);
    const right = travelsal(node.right);
    const doNot =  Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
    const doit = node.val + left[0] + right[0];
    return [doNot,doit]
}
// @lc code=end

