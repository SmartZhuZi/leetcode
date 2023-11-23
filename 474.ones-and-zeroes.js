/*
 * @lc app=leetcode id=474 lang=javascript
 *
 * [474] Ones and Zeroes
 */

// @lc code=start
/**
 * @param {string[]} strs
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var findMaxForm = function(strs, m, n) {
    let dp = new Array(m+1).fill().map(()=> new Array(n+1).fill(0));
    for (let i=0; i<strs.length;i++){
        let x=0,y=0;
        for (let temp=0;temp < strs[i].length;temp++){
            if (strs[i][temp] === '0'){
                x+=1;
            }
            else{
                y+=1;
            }
        }
        for (let j=m;j>=x;j--){
            for (let k=n;k>=y;k--){
                dp[j][k] = Math.max(dp[j][k],dp[j-x][k-y]+1);
            }
        }
    }

    return dp[m][n]
};
// @lc code=end

