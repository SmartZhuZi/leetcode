/*
 * @lc app=leetcode id=121 lang=javascript
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let dp = Array(prices.length).fill().map(()=>[0,0]);
    dp[0] = [-prices[0],0];
    // console.log(dp)
    for (let i=1;i<prices.length;i++){
        dp[i][0] = Math.max(-prices[i],dp[i-1][0]);
        dp[i][1] = Math.max(dp[i-1][1], dp[i-1][0]+prices[i]);
    };
    return dp[prices.length-1][1];
};
// @lc code=end

