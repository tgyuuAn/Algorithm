class Solution {
    fun check(removeCnt: Int, rocks: List<Int>, minDistance: Int): Boolean{
        var remain = removeCnt
        var prev = rocks[0]
        for(dist in rocks.subList(1, rocks.size)){
            if(dist-prev < minDistance){
                if(remain == 0){
                    return false
                }
                remain -= 1
                continue
            }
            
            prev = dist
        }
        
        return true
    }
    
    fun solution(distance: Int, rocks: IntArray, n: Int): Int {
        val rocks = rocks.toMutableList()
        rocks.add(0)
        rocks.add(distance)
        rocks.sort()
        var answer = 0
        var left = 0
        var right = 1_000_000_001
        while(left+1<right){
            val mid = (left+right)/2            
            if(check(removeCnt = n, rocks = rocks, minDistance = mid)){
                answer = mid
                left = mid
            } else {
                right = mid
            }
        }
        
        return answer
    }
}