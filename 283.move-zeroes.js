/*
 * @lc app=leetcode id=283 lang=javascript
 *
 * [283] Move Zeroes
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let slow = 0;
    // fast = 1;
    for (let fast=0;fast<nums.length;fast++){
        if (nums[fast] !== 0){
            nums[slow] = nums[fast];
            slow += 1;
        }
        // fast+=1;
    }
    for (let i=slow;i<nums.length;i++){
        nums[i] = 0;
    }
};
// @lc code=end

