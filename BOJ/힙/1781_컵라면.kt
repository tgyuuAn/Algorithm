import java.util.*

fun main() {
    val br = System.`in`.bufferedReader()
    val N = br.readLine().toInt()

    val sequence = mutableListOf<Pair<Long, Long>>()
    repeat(N) {
        val (deadline, score) = br.readLine().split(" ").map{ it.toLong() }
        sequence.add(deadline to score)
    }
    sequence.sortWith(compareBy({ it.first }, { -it.second }))

    val priority = PriorityQueue<Pair<Long, Long>>(Comparator { a, b -> 
        a.second.compareTo(b.second)
    })
    
    for ((d, sc) in sequence) {
        if (priority.size < d) {
            priority.offer((d to sc))
            continue
        }

        val (_, min_sc) = priority.peek()
        if (min_sc < sc) {
            priority.poll()
            priority.offer((d to sc))
        }
    }
    
    println(priority.map{ it.second }.sum())
}
