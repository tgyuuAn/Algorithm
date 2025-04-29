class Solution {
    
    val answer = mutableSetOf<String>()
    lateinit var questions: List<Set<Int>>
    lateinit var answers: IntArray
    
    fun solution(n: Int, q: Array<IntArray>, ans: IntArray): Int {
        questions = q.map { it.toSet() }
        answers = ans
        
        val now = mutableListOf<Int>()
        dfs(n, now, 0)
        
        return answer.size
    }
    
    fun dfs(n: Int, now: MutableList<Int>, lastIdx: Int) {
        if (now.size == questions[0].size) {
            if (check(now)) {
                val sb = StringBuilder()
                now.forEach {
                    sb.append(it.toString())
                }
                answer.add(sb.toString())
            }
            return
        }
        
        if (lastIdx == n) return

        
        for (idx in (lastIdx+1)..n) {
            now.add(idx)
            dfs(n, now, idx)
            now.removeLast()
        }
    }
    
    fun check(status: MutableList<Int>) : Boolean {
        for (idx in 0 until questions.size) {
            val question = questions[idx]
            val answer = answers[idx]
            
            var count = 0
            for (elem in status) {
                if (elem in question) count += 1
            }
            
            if (count != answer) return false
        }
        
        return true
    }
}