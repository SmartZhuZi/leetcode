/*
 * @lc app=leetcode id=213 lang=javascript
 *
 * [213] House Robber II
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if (nums.length === 0) return 0;
    if (nums.length === 1) return nums[0];
    return Math.max(basic_rob(nums.slice(0,nums.length-1)),basic_rob(nums.slice(1,nums.length)));
};

const basic_rob = (nums)=>{
    let dp = Array(nums.length).fill(0);
    dp[0] = nums[0];
    dp[1] = Math.max(nums[0],nums[1]);
    for (let i=2;i<nums.length;i++){
        dp[i] = Math.max(dp[i-2]+nums[i],dp[i-1]);
    }
    return dp[nums.length-1];
};
// @lc code=end

