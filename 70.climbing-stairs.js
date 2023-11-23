/*
 * @lc app=leetcode id=70 lang=javascript
 *
 * [70] Climbing Stairs
 */

// @lc code=start
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    dp = Array(n+1).fill(0);
    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 2;
    climb = new Array(1,2);
    // console.log(climb)
    for (let i=3;i<=n;i++){
        for (let j of climb){
            dp[i] += dp[i-j];
            // console.log(i,j);
            // console.log(dp)
        }
    }
    return dp[n]
};
// @lc code=end

