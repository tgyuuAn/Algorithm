import java.util.*

class Solution {
    fun solution(n: Int, costs: Array<IntArray>): Int {
        var answer = 0
        val graph = IntArray(n+1) { it }
        val nodes = PriorityQueue<IntArray>(Comparator { a,b ->
            a[2].compareTo(b[2])
        })
        
        for (cost in costs) {
            nodes.offer(cost)
        }
        
        while (!nodes.isEmpty()) {
            val popped = nodes.poll()
            val start = popped[0]
            val end = popped[1]
            val cost = popped[2]
            
            if (union(start, end, graph)) {
                answer += cost
            }
        }
        
        return answer
    }
    
    fun union(x: Int, y: Int, graph: IntArray): Boolean {
        val xParent = findParent(x, graph)
        val yParent = findParent(y, graph)
        
        if (xParent == yParent) return false
        
        if (xParent < yParent) {
            graph[yParent] = xParent
        } else {
            graph[xParent] = yParent
        }
        return true
    }
    
    fun findParent(child: Int, graph: IntArray): Int {
        if (child == graph[child]) return child
        
        val parent = graph[child]
        graph[child] = findParent(parent, graph)
        return graph[child]
    }
}