/*
 * @lc app=leetcode id=347 lang=javascript
 *
 * [347] Top K Frequent Elements
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let hash_dict = {};
    for (let i=0;i<nums.length;i++){
        if (hash_dict[nums[i]] !== undefined){
            hash_dict[nums[i]] += 1;
        }
        else{
            hash_dict[nums[i]] = 1;
        }
    }
    let top_k = [];
    for (let [key,value] of Object.entries(hash_dict)){
        top_k.push([value,parseInt(key)]);
    }
    top_k.sort((a,b) => {
        return b[0]-a[0];
    })
    let result = [];
    for (let i=0;i<k;i++){
        result.push(top_k[i][1]);
    }
    return result
};
// @lc code=end

