import kotlin.math.*

class Solution {
    fun solution(diffs: IntArray, times: IntArray, limit: Long): Int {
        var left = 0
        var right = diffs.toList().maxOrNull()!! + 1
        while (left+1<right) {
            val mid = (left+right)/2
            
            if (check(mid, diffs, times, limit)) {
                // 현재 숙련도로 통과 가능하다면
                right = mid
            } else {
                // 현재 숙련도로 불가능 하다면
                left = mid                
            }
        }
        
        return right
    }
    
    fun check(mid: Int, diffs: IntArray, times: IntArray, limit:Long) : Boolean {
        var temp = 0L
        for (idx in 0 until diffs.size) {
            val diff = diffs[idx]
            val timeCur = times[idx]
            val timePrev = if (idx != 0) times[idx-1] else 0
            
            val count = (diff-mid).coerceAtLeast(0)
            temp += count*(timeCur+timePrev).toLong()
            temp += timeCur.toLong()
            
            if (temp > limit) return false
        }
        
        return true
    }
}