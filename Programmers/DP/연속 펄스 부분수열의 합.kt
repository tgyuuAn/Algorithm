import kotlin.math.*

class Solution {
    fun solution(sequence: IntArray): Long {
        val ex1 = sequence.toList()
            .mapIndexed{ idx, elem -> 
                if(idx%2==0){
                    elem * -1
                } else { 
                    elem
                }
            }
        
        val dp1 = MutableList<Long>(sequence.size){ 0 }
        dp1[0] = ex1[0].toLong()
        
        for(idx in 1 until sequence.size){
            dp1[idx] = max(dp1[idx-1] + ex1[idx].toLong(), ex1[idx].toLong())
        }
        
        val ex2 = sequence.toList()
            .mapIndexed{ idx, elem -> 
                if(idx%2==1){
                    elem * -1
                } else { 
                    elem
                }
            }
        
        val dp2 = MutableList<Long>(sequence.size){ 0 }
        dp2[0] = ex2[0].toLong()
        
        for(idx in 1 until sequence.size){
            dp2[idx] = max(dp2[idx-1] + ex2[idx].toLong(), ex2[idx].toLong())
        }
        
        return max(dp1.maxOrNull() ?: 0, dp2.maxOrNull() ?: 0).toLong()
    }
}