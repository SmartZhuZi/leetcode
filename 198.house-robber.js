/*
 * @lc app=leetcode id=198 lang=javascript
 *
 * [198] House Robber
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    dp = Array(nums.length).fill(0);
    dp[0] = nums[0];
    dp[1] = Math.max(nums[0],nums[1]);
    for (let i=2;i<nums.length;i++){
        dp[i] = Math.max(dp[i-2]+nums[i],dp[i-1]);
    }
    // console.log(dp)
    return dp[nums.length-1];
};
// @lc code=end

