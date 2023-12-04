/*
 * @lc app=leetcode id=35 lang=javascript
 *
 * [35] Search Insert Position
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    let low = 0;
    let high = nums.length;
    while (low < high){
        let mid = low + Math.floor((high-low)/2);
        if (nums[mid] > target){
            high = mid;
        }
        else if (nums[mid] < target){
            low = mid+1;
        }
        else{
            return mid;
        }
    }
    return high
};
// @lc code=end

