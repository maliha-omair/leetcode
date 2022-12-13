/**
 * @param {number} n
 * @return {number}
 */

let mem = []


var climbStairs = function(n){
    for( let i=0;i<45;i++){
        mem[i] = 0;
    }
    return climbStairsHelper(n)
}

var climbStairsHelper = function(n) {
    if(n<1) return 0
    if(n===1) return 1
    if(n===2) return 2

    if(mem[n-1] === 0){
        mem[n-1] = climbStairsHelper(n-1)
    }
    if(mem[n-2] === 0){
        mem[n-2] = climbStairsHelper(n-2)
    }

    return  mem[n-1] + mem[n-2]
};
