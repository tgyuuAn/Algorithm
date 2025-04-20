import java.util.*

fun main() {
    val br = System.`in`.bufferedReader()
    val N = br.readLine().toInt()

    if (N == 1) {
        println(0)
        return
    }
    
    val xCoordintaes = mutableListOf<Pair<Long, Int>>()
    val yCoordintaes = mutableListOf<Pair<Long, Int>>()
    val zCoordintaes = mutableListOf<Pair<Long, Int>>()

    repeat(N) { idx ->
        val _input = br.readLine().split(" ").map{ it.toLong() }
        xCoordintaes.add(_input[0] to idx)
        yCoordintaes.add(_input[1] to idx)
        zCoordintaes.add(_input[2] to idx)
    }
    
    xCoordintaes.sortBy { it.first } 
    yCoordintaes.sortBy { it.first }
    zCoordintaes.sortBy { it.first }
    
    val xGaps = PriorityQueue<Triple<Long, Int, Int>>(compareBy { it.first })
    val yGaps = PriorityQueue<Triple<Long, Int, Int>>(compareBy { it.first })
    val zGaps = PriorityQueue<Triple<Long, Int, Int>>(compareBy { it.first })
    
    for (idx in 1 until xCoordintaes.size) {
        val gap = xCoordintaes[idx].first - xCoordintaes[idx-1].first
        xGaps.offer(Triple(gap, xCoordintaes[idx].second, xCoordintaes[idx-1].second))
    }
    
    for (idx in 1 until yCoordintaes.size) {
        val gap = yCoordintaes[idx].first - yCoordintaes[idx-1].first
        yGaps.offer(Triple(gap, yCoordintaes[idx].second, yCoordintaes[idx-1].second))
    }
    
    for (idx in 1 until zCoordintaes.size) {
        val gap = zCoordintaes[idx].first - zCoordintaes[idx-1].first
        zGaps.offer(Triple(gap, zCoordintaes[idx].second, zCoordintaes[idx-1].second))
    }
    
    val parentGraph = MutableList<Int>(N){ it }
    var answer = 0L
    var edgeCount = 0
    while (edgeCount < N - 1) {
        val xPeek = xGaps.peek()?.first ?: Long.MAX_VALUE
        val yPeek = yGaps.peek()?.first ?: Long.MAX_VALUE
        val zPeek = zGaps.peek()?.first ?: Long.MAX_VALUE
        
        when {
            xPeek <= yPeek && xPeek <= zPeek -> {
                val polledGap = xGaps.poll()
                
                if (union(polledGap.second, polledGap.third, parentGraph)) {
                    answer += polledGap.first
                    edgeCount += 1
                }
            }
            
            yPeek <= xPeek && yPeek <= zPeek -> {
                val polledGap = yGaps.poll()
                
                if (union(polledGap.second, polledGap.third, parentGraph)) {
                    answer += polledGap.first
                    edgeCount += 1
                }
            }
            
            zPeek <= xPeek && zPeek <= yPeek -> {
                val polledGap = zGaps.poll()

                if (union(polledGap.second, polledGap.third, parentGraph)) {
                    answer += polledGap.first
                    edgeCount += 1
                }
            }
        }
    }
    
    println(answer)
}

fun find_parent(element: Int, graph: MutableList<Int>) : Int {
    if (element != graph[element]) {
        graph[element] = find_parent(graph[element], graph)
    }
    return graph[element]
}

fun union(x: Int, y: Int, graph: MutableList<Int>) : Boolean {
    val first = find_parent(x, graph)
    val second = find_parent(y, graph)
    
    if (first == second) return false
    if (first < second) graph[second] = first else graph[first] = second
    return true
}