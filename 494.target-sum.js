/*
 * @lc app=leetcode id=494 lang=javascript
 *
 * [494] Target Sum
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var findTargetSumWays = function(nums, target) {
    sum = nums.reduce((a,b)=> a+b);
    if (Math.abs(target) > sum){
        return 0;
    }
    if ((target+sum) / 2 !== Math.floor((target+sum)/2)){
        return 0;
    }
    else {
        left = (target+sum) / 2;
    }
    let dp = Array(left+1).fill(0);
    dp[0] = 1
    for (i=0;i<nums.length;i++){
        for(j=left;j>=nums[i];j--){
            dp[j] += dp[j-nums[i]]
        }
    }
    // console.log(dp)
    return(dp[left])
};
// @lc code=end

