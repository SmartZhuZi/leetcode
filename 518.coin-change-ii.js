/*
 * @lc app=leetcode id=518 lang=javascript
 *
 * [518] Coin Change II
 */

// @lc code=start
/**
 * @param {number} amount
 * @param {number[]} coins
 * @return {number}
 */
var change = function(amount, coins) {

    let dp = Array(amount+1).fill(0);
    dp[0]=1;
    for (let i=0; i<coins.length; i++){
        for (let j=coins[i]; j<=amount; j++){
            dp[j] += dp[j-coins[i]];
        }
    }
    // console.log(dp);
    return dp[amount]
};
// @lc code=end

