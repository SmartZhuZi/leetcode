/*
 * @lc app=leetcode id=1049 lang=javascript
 *
 * [1049] Last Stone Weight II
 */

// @lc code=start
/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeightII = function(stones) {
    sum = stones.reduce((accumulator,current) => accumulator + current,0);
    target = Math.floor(sum / 2);
    dp = Array(100001).fill(0);
    for (let i=0;i < stones.length; i++){
        for (let j=target; j>=stones[i]; j--){
            dp[j] = Math.max(dp[j],dp[j-stones[i]]+stones[i]);
        }
    }
    // console.log(dp)
    return sum - dp[target] - dp[target]
};
// @lc code=end

