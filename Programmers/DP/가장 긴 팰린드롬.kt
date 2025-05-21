class Solution {
    fun solution(s: String): Int {
        var answer = 1
        val DP = Array(s.length){ IntArray(s.length){ 0 } }
        
        for(idx in s.indices) {
            DP[idx][idx] = 1
        }
        
        for(idx in 0 until s.length-1) {
            if(s[idx] == s[idx+1]) {
                DP[idx][idx+1] = 1
                answer = 2
            }
        }
        
        for(step in 2 until s.length) {
            for(idx in 0 until s.length-step) {
                // 만약 이전 항목이 팰린드롬이었다면,
                if(DP[idx+1][idx+step-1]==1) {
                    if(s[idx] == s[idx+step]) {
                        DP[idx][idx+step] = 1
                        answer = maxOf(answer, step+1)
                    }
                }
            }
        }
        
        return answer
    }
}