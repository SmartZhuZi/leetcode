/*
 * @lc app=leetcode id=115 lang=javascript
 *
 * [115] Distinct Subsequences
 */

// @lc code=start
/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var numDistinct = function(s, t) {
    //dp definiation (how many ways of the dp[i-1][j-1] )
    const dp = Array(s.length+1).fill(0).map(()=> Array(t.length+1).fill(0));
    for (let i=0;i<=s.length;i++){
        dp[i][0] = 1;
    };
    // console.log(dp);
    for (let i=1;i<=s.length;i++){
        for (let j=1;j<=t.length;j++){
            if (s[i-1] === t[j-1]){
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
            }
            else{
                dp[i][j] = dp[i-1][j];
            }
        }
    }
    // console.log(dp);
    return dp[s.length][t.length]
    
};
// @lc code=end

