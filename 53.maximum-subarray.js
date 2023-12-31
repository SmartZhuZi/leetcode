/*
 * @lc app=leetcode id=53 lang=javascript
 *
 * [53] Maximum Subarray
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    const dp = Array(nums.length).fill(0);
    dp[0]=nums[0]
    let result = nums[0];
    for (let i=1;i<nums.length;i++){
        dp[i] = Math.max(dp[i-1]+nums[i],nums[i]);
        if (dp[i] > result){
            result = dp[i];
        };
    };
    // console.log(dp);
    return result;

};
// @lc code=end

