/*
 * @lc app=leetcode id=123 lang=javascript
 *
 * [123] Best Time to Buy and Sell Stock III
 */

// @lc code=start
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    dp = Array(prices.length).fill().map(()=>[0,0,0,0,0]);
    dp[0][1] = -prices[0];
    dp[0][3] = -prices[0];
    // console.log(dp)
    for (let i=1;i<prices.length;i++){
        // first sell the stock
        dp[i][1] = Math.max(dp[i-1][1],-prices[i]);
        dp[i][2] = Math.max(dp[i-1][2],dp[i-1][1]+prices[i]);
        dp[i][3] = Math.max(dp[i-1][3],dp[i-1][2]-prices[i]);
        dp[i][4] = Math.max(dp[i-1][4],dp[i-1][3]+prices[i]);
    }
    return dp[prices.length-1][4];
};
// @lc code=end

