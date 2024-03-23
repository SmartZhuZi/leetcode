/*
 * @lc app=leetcode id=844 lang=javascript
 *
 * [844] Backspace String Compare
 */

// @lc code=start
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function(s, t) {
    const build = (str) => {
        let result = [];
        for (let chr of str){
            if (chr !== '#'){
                result.push(chr);
            }
            else if (result.length > 0){
                result.pop();
            };
        };
        return result.join('');
    };
    return build(s) === build(t);
};
// @lc code=end

