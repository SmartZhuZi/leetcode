/*
 * @lc app=leetcode id=188 lang=javascript
 *
 * [188] Best Time to Buy and Sell Stock IV
 */

// @lc code=start
/**
 * @param {number} k
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(k, prices) {
    dp = Array(prices.length).fill().map(()=> Array(2*k+1).fill(0));
    for (let i=0;i<k; i++){
        dp[0][2*i+1] = -prices[0];
    }
    // console.log(dp)
    for (let i=1;i<prices.length;i++){
        for (let j=0;j<2*k+1;j+=2){
            dp[i][j+1] = Math.max(dp[i-1][j+1],dp[i-1][j]-prices[i]);
            dp[i][j+2] = Math.max(dp[i-1][j+2],dp[i-1][j+1]+prices[i]);
        }
    }
    return dp[prices.length-1][2*k];
};
// @lc code=end

