class Solution {
    var answer = 0
    val brackets = listOf('(', ')')
    
    fun solution(n: Int): Int {
        val now = mutableListOf<Char>()
        dfs(now, n, 0)
        return answer
    }
    
    fun dfs(now: MutableList<Char>, maxPairCount: Int, openCount: Int) {
        if (now.size == maxPairCount*2) {
            if (checkBracket(now)) answer += 1
            return
        }
        
        for (elem in brackets) {
            if (elem == '(' && openCount >= maxPairCount) continue
            if (elem == ')' && (now.size-openCount)>=openCount) continue
            
            var newOpenCount = if(elem == '(') openCount+1 else openCount
            now.add(elem)
            dfs(now, maxPairCount, newOpenCount)
            now.removeLast()
        }
    }
    
    fun checkBracket(bracket: MutableList<Char>): Boolean {
        var openCount = 0
        for (elem in bracket) {
            if (elem == '(') openCount += 1
            else {
                if (openCount <= 0) return false
                else openCount -= 1
            }
        }
        
        if (openCount != 0) return false
        return true
    }
}