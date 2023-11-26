/*
 * @lc app=leetcode id=122 lang=javascript
 *
 * [122] Best Time to Buy and Sell Stock II
 */

// @lc code=start
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    dp = Array(prices.length).fill().map(()=>[0,0]);
    dp[0][0] = -prices[0];
    dp[0][1] = 0;
    // console.log(dp);
    for (i=1;i<prices.length;i++){
        dp[i][0] = Math.max(dp[i-1][0],dp[i-1][1]-prices[i]);
        dp[i][1] = Math.max(dp[i-1][1],dp[i-1][0]+prices[i]);
    }
    // console.log(dp);
    return dp[prices.length-1][1];
};
// @lc code=end

