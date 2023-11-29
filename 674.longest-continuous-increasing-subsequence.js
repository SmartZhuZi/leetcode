/*
 * @lc app=leetcode id=674 lang=javascript
 *
 * [674] Longest Continuous Increasing Subsequence
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var findLengthOfLCIS = function(nums) {
    const dp = Array(nums.length).fill(1);
    let result = 1;
    for(let i=1;i<nums.length;i++){
        if (nums[i]>nums[i-1]){
            dp[i]= dp[i-1]+1;
        }
        result = Math.max(dp[i],result);
        }
    return result;
    };
// @lc code=end

