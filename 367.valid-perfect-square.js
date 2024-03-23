/*
 * @lc app=leetcode id=367 lang=javascript
 *
 * [367] Valid Perfect Square
 */

// @lc code=start
/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function(num) {
    if (num<2){
        return true;
    }
    let low = 1;
    let high = Math.floor(num/2);
    while(low<=high){
        let mid = Math.floor((high+low)/2);
        if (mid*mid > num){
            high = mid-1;
        }
        else if (mid*mid < num){
            low = mid+1;
        }
        else{
            return true;
        }
    }
    return false;
};
// @lc code=end

