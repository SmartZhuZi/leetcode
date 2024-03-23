/*
 * @lc app=leetcode id=69 lang=javascript
 *
 * [69] Sqrt(x)
 */

// @lc code=start
/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    if (x<2){
        return x;
    }
    let low = 1;
    let high = Math.floor(x/2);
    while (low < high){
        let mid = low + Math.floor((1+high-low)/2);
        if (mid*mid > x){
            high = mid - 1;
        }
        else {
            low = mid;
        }
    }
    return low;
};
// @lc code=end

