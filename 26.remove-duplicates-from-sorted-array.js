/*
 * @lc app=leetcode id=26 lang=javascript
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    if (nums.length <= 1){
        return nums.length;
    }
    let slow = 0;
    // let fast = 1;
    for (let fast=1;fast<nums.length;fast++){
        if (nums[slow] !== nums[fast]){
            slow += 1;
            nums[slow] = nums[fast];
            
        }
    }
    return slow+1;
};
// @lc code=end

