/**  Leetcode #295 */
var MedianFinder = function() {
    arr = []
};

/** 
 * @param {number} num
 * @return {void}
 */
MedianFinder.prototype.addNum = function(num) {
    
    arr.push(num) 

};

/**
 * @return {number}
 */
MedianFinder.prototype.findMedian = function() {
  
    arr = arr.sort(function(a, b){return a - b})
    
    if (arr.length ==1)
    {
        return arr[0]
    }

    if (arr.length % 2 == 0)
    {

        output = (arr[Math.floor((arr.length)/2)-1] + arr[Math.floor((arr.length)/2) ]) / 2
        return output
      
    } else 
      
    {
        return arr[Math.floor((arr.length)/2)]
    }
    
};

/** 
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */
