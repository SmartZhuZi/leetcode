/*
 * @lc app=leetcode id=96 lang=javascript
 *
 * [96] Unique Binary Search Trees
 */

// @lc code=start
/**
 * @param {number} n
 * @return {number}
 */
var numTrees = function(n) {
    dp = Array(n+1).fill(0)
    dp[0] = 1
    // dp[1] = 1
    for (let i=1;i<=n;i++){
        for (let j =1 ;j<=i;j++){
            dp[i] += dp[j-1] * dp[i-j]
        }
    }
    console.log(dp)
    return dp[n]
    
};
// @lc code=end

