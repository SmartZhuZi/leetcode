/*
 * @lc app=leetcode id=34 lang=javascript
 *
 * [34] Find First and Last Position of Element in Sorted Array
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    const findleft = ()=>{
        let left=0;
        let right=nums.length;
        while(left<right){
            
            let mid = left+Math.floor((right-left)/2);
            // console.log(left,right,mid);
            if (nums[mid] >= target){
                right = mid;    
            }
            else {
                left = mid+1;
            }}
        return right;
    };

    const findright = () =>{
        let left=0;
        let right=nums.length;
        while (left < right){
            let mid = left+Math.floor((right-left)/2);
            if (nums[mid] > target){
                right = mid;
            }
            else {
                left = mid+1;
            }
            
        }
        return left-1;
    };
    // console.log(findleft(),findright())
    let leftindex = findleft();
    let rightindex = findright();
    if (leftindex <= rightindex && rightindex < nums.length && nums[leftindex] === target && nums[rightindex] === target) {
        return [leftindex, rightindex];
    }
    return [-1, -1];
};
// @lc code=end

