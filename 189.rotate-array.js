/*
 * @lc app=leetcode id=189 lang=javascript
 *
 * [189] Rotate Array
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    //    辅助数组方法
    k %= nums.length;
    const temp = [];
    for (let i=nums.length-k;i<nums.length;i++){
        temp.push(nums[i]);
    }
    for (let i=0;i<nums.length-k;i++){
        temp.push(nums[i]);
    }
    for (let i=0;i<temp.length;i++){
        nums[i] = temp[i]
    }

}
// @lc code=end

