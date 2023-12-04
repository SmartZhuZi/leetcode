/*
 * @lc app=leetcode id=27 lang=javascript
 *
 * [27] Remove Element
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let slow = 0;
    let fast = 0;
    for (let i=0;i<nums.length;i++){
        if (nums[fast] !== val){
            nums[slow] = nums[fast];
            slow +=1;
        }
        fast += 1;
    }
    return slow
};
// @lc code=end

