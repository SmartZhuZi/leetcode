/*
 * @lc app=leetcode id=300 lang=javascript
 *
 * [300] Longest Increasing Subsequence
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
    let dp = new Array(nums.length).fill(1);
    let result = 0;
    for (let i=0;i<nums.length;i++){
        for(let j=0;j<i;j++){
            if (nums[j]<nums[i]){
            dp[i] = Math.max(dp[i],dp[j]+1)
        };
        };
        result = Math.max(result,dp[i]);
    };
    return result;
};
// @lc code=end

