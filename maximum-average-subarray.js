/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    let sum = 0
    let start = 0 
    let result = []
    
    console.log("array length ...", nums.length)
    for (let end=0; end<nums.length; end++ ){
        sum = sum + nums[end]

        if(end >= k-1){
            let avg = sum/k
//            console.log("average ...",avg)
            result.push(avg)          
            sum = sum - nums[start]
            start = start + 1 
        }
    }
    
    let maxAvg = result[0];
    for(let i= 1 ; i< result.length; i++){
        if( maxAvg < result[i] ){
            maxAvg = result[i]
        }
    }
    return maxAvg;
};
