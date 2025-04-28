import java.util.*

fun main() {
    val br = System.`in`.bufferedReader()
    val N = br.readLine().toInt()
    
    val stationList = mutableListOf<Pair<Int, Int>>()
    repeat(N) {
        val (a, b) = br.readLine().split(" ").map{ it.toInt() }
        stationList.add(a to b)
    }
    
    stationList.sortBy { it. first }
    val stations = ArrayDeque<Pair<Int, Int>>(stationList)

    val (L, P) = br.readLine().split(" ").map{ it.toInt() }
    val reachable = PriorityQueue<Pair<Int, Int>>(Comparator { a, b ->
        b.second.compareTo(a.second)
    })
    
    var count = 0
    var now = P
    while (now < L && !(stations.isEmpty() && reachable.isEmpty())) {
        while (!stations.isEmpty()) {
            var (distance, gas) = stations.first
            if (now >= distance) {
                reachable.offer(stations.removeFirst())
            } else {
                break
            }
        }
        
        if (!reachable.isEmpty()) {
            val (_, chargedGas) = reachable.poll()
            now += chargedGas
            count += 1
        } else {
            break
        }
    }
    
    if (now >= L) {
        println(count)
    } else {
        println(-1)
    }
}