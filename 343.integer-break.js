/*
 * @lc app=leetcode id=343 lang=javascript
 *
 * [343] Integer Break
 */

// @lc code=start
/**
 * @param {number} n
 * @return {number}
 */
var integerBreak = function (n) {
    let dp = Array(n + 1).fill(0);
    dp[2] = 1
    for (let i = 3; i <= n; i++) {
        for (let j = 1; j <= i / 2; j++) {
            dp[i] = Math.max(dp[i], j * (i - j), j * dp[i - j]);
        }
    }
    return dp[n]
};
// @lc code=end

