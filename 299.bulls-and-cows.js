/*
 * @lc app=leetcode id=299 lang=javascript
 *
 * [299] Bulls and Cows
 */

// @lc code=start
/**
 * @param {string} secret
 * @param {string} guess
 * @return {string}
 */
var getHint = function(secret, guess) {
    // console.log(secret,guess)
    let A=0;
    let B=0;
    const hash = Array(10).fill(0);
    for (let i=0;i<secret.length;i++){
        if (guess[i] === secret[i]){
            A+=1;
        }
        else{
            hash[secret[i].charCodeAt() - '0'.charCodeAt()] += 1;
        }
    };
    for (let i=0;i<guess.length;i++){
        if (secret[i] !== guess[i] && hash[guess[i].charCodeAt() - '0'.charCodeAt()] > 0){
            B++;
            hash[guess[i].charCodeAt() - '0'.charCodeAt()]--;
        }
    }
    return `${A}A${B}B`;

};
// @lc code=end

