/*
 * @lc app=leetcode id=49 lang=javascript
 *
 * [49] Group Anagrams
 */

// @lc code=start
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let hash_dict = {};
    for (let i = 0;i<strs.length;i++){
        sorted = strs[i].split("").sort().join("");
        if (hash_dict[sorted] !== undefined){
            hash_dict[sorted].push(strs[i]);
        }
        else{
            let arr = [strs[i]];
    
            hash_dict[sorted] = arr;

        } 
    }
    // console.log(hash_dict)
    let result = Object.values(hash_dict);
    return result;
};

// @lc code=end

