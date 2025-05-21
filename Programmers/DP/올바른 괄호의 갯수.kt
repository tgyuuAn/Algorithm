class Solution {
    fun solution(n: Int): Int {
        val dpTable = IntArray(n+1){ 0 }
        dpTable[0] = 1
        dpTable[1] = 1
        
        for (idx in 2..n) {
            for (inBracket in 0 until idx) {
                val outBracket = (idx-1)-inBracket
                dpTable[idx] = dpTable[idx] + (dpTable[inBracket] * dpTable[outBracket])
            }
        }
        
        return dpTable[n]
    }
}