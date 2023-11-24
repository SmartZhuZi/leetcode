/*
 * @lc app=leetcode id=139 lang=javascript
 *
 * [139] Word Break
 */

// @lc code=start
/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    let dp = Array(s.length+1).fill(false);
    dp[0] = true;
    for (let i=1;i<=s.length;i++){
        for (let j=0;j<wordDict.length;j++){
            if (i>= wordDict[j].length){
                if (s.slice(i - wordDict[j].length, i) === wordDict[j] && dp[i-wordDict[j].length]){
                    dp[i] = true;
                }
            }
        }
    }
    // console.log(dp);
    return dp[s.length];
};
// @lc code=end

