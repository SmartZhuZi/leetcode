/*
 * @lc app=leetcode id=63 lang=javascript
 *
 * [63] Unique Paths II
 */

// @lc code=start
/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function(obstacleGrid) {
    var m = obstacleGrid.length;
    var n = obstacleGrid[0].length;
    var dp = Array(m).fill(0).map( () => Array(n).fill(0) )

    for (var i=0;i<m && obstacleGrid[i][0] === 0; i++){
        dp[i][0] = 1;
    }
    for (var i=0;i<n && obstacleGrid[0][i] === 0; i++){
        dp[0][i] = 1;
    }

    for (var i=1; i<m;i++){
        for (var j=1; j<n ;j++ ){
            if (obstacleGrid[i][j] === 1){
                continue;
            }
            else{
                dp[i][j] = dp[i-1][j]+dp[i][j-1];
            }
        }
    }
    return dp[m-1][n-1]
};
// @lc code=end

