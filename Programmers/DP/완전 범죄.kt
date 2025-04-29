import kotlin.math.*

class Solution {
    fun solution(info: Array<IntArray>, n: Int, m: Int): Int {
        val dpTable = Array(info.size+1) { idx -> IntArray(m+1) { 
            if (idx==0) 0 else -1        
            } 
        }
        
        for (idx in 0 until info.size) {
            val (a, b) = info[idx]
            
            for (bIdx in 0 until m) {
                if (dpTable[idx][bIdx] == -1) continue
                
                // B가 훔쳤을 때
                if (bIdx+b < m) {
                    if (dpTable[idx+1][bIdx+b] == -1) {
                        dpTable[idx+1][bIdx+b] = dpTable[idx][bIdx]
                    } else {
                        dpTable[idx+1][bIdx+b] = min(dpTable[idx+1][bIdx+b], dpTable[idx][bIdx])
                    }
                }
                
                // A가 훔쳤을 때
                if (dpTable[idx+1][bIdx] == -1) {
                    dpTable[idx+1][bIdx] = dpTable[idx][bIdx] + a
                } else if (dpTable[idx][bIdx] + a < n) {
                    dpTable[idx+1][bIdx] = min(dpTable[idx+1][bIdx], dpTable[idx][bIdx] + a )
                }
            }
        }
        
        var answer: Int = -1
        for (temp in dpTable[info.size]){
            if (temp == -1) continue
            
            if (answer == -1) {
                answer = temp
                continue
            }
            
            answer = min(answer, temp)
        }
        return if (answer < n) answer else -1
    }
}