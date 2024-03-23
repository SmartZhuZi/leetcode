/*
 * @lc app=leetcode id=1 lang=javascript
 *
 * [1] Two Sum
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let seen = {};
    for (let i=0;i<nums.length;i++){
        seek = target-nums[i]
        if (seen[seek] !== undefined){
            return [i,seen[seek]];
        }
        seen[nums[i]] = i;
    }
};
// @lc code=end

