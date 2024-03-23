/*
 * @lc app=leetcode id=242 lang=javascript
 *
 * [242] Valid Anagram
 */

// @lc code=start
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
   const hash_record = new Array(26).fill(0);
   for(let i=0;i<s.length;i++){
    hash_record['z'.charCodeAt('A')-s[i].charCodeAt('A')] += 1;
   }
   for (let i=0;i<t.length;i++){
    hash_record['z'.charCodeAt('A')-t[i].charCodeAt('A')] -= 1;
   }
   console.log(hash_record);
   for (let i=0;i<hash_record.length;i++){
    if (hash_record[i] !== 0){
        return false;
    }
   }
   return true;
};
// @lc code=end

