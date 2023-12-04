/*
 * @lc app=leetcode id=41 lang=javascript
 *
 * [41] First Missing Positive
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    let n = nums.length;
    for (let i=0;i<n;i++){
        while (nums[i] > 0 && nums[i] < nums.length && nums[nums[i]-1] !== nums[i]){
            let temp = nums[nums[i]-1];
            nums[nums[i]-1] = nums[i];
            nums[i] = temp; 
        }
    }
    for (let i=0;i<nums.length;i++){
        if (nums[i] != i+1){
            return i+1;
        }
    }
    return n+1;
};
// @lc code=end

