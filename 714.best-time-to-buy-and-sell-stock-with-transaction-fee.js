/*
 * @lc app=leetcode id=714 lang=javascript
 *
 * [714] Best Time to Buy and Sell Stock with Transaction Fee
 */

// @lc code=start
/**
 * @param {number[]} prices
 * @param {number} fee
 * @return {number}
 */
var maxProfit = function(prices, fee) {
    dp = Array(prices.length).fill().map(()=>[0,0]);
    dp[0][0] = -prices[0];
    for (let i=1;i<prices.length;i++){
        dp[i][0] = Math.max(dp[i-1][0],dp[i-1][1]-prices[i]);
        dp[i][1] = Math.max(dp[i-1][1],dp[i-1][0]+prices[i]-fee);
    };
    // console.log(dp);
    return dp[prices.length-1][1];
};
// @lc code=end

