class Solution {
    fun solution(n: Int, w: Int, num: Int): Int {
        val totalFloor = (n-1) / w
        val numFloor   = (num-1) / w
        val topCnt     = (n-1) % w + 1 
        val col = if (numFloor % 2 == 0) (num-1) % w + 1 else w - ((num-1) % w)      

        var answer = totalFloor - numFloor
        
        if (totalFloor % 2 == 0) {
            if (col > topCnt) answer--
        } else {
            if (col <= w - topCnt) answer--
        }
        
        return answer + 
    }
}