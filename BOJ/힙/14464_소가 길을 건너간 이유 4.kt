import java.util.*

fun main() {
    val br = System.`in`.bufferedReader()
    val (C, N) = br.readLine().split(" ").map(String::toInt)

    val chickens = List(C) { br.readLine().toInt() }.sorted()
    val cows = List(N) {
        br.readLine().split(" ").map(String::toInt).let { (a, b) -> a to b }
    }.sortedBy { it.first }
    
    val pq = PriorityQueue<Int>()

    var idx = 0
    var answer = 0

    for (T in chickens) {
        while (idx < N && cows[idx].first <= T) {
            pq.offer(cows[idx].second)
            idx++
        }

        while (pq.isNotEmpty() && pq.peek() < T) {
            pq.poll()
        }

        if (pq.isNotEmpty()) {
            pq.poll()
            answer++
        }
    }

    println(answer)
}
