import java.util.*

fun main() {
    val br = System.`in`.bufferedReader()
    val (K, N) = br.readLine().split(" ").map{ it.toInt() }
    val origin = br.readLine().split(" ").map{ it.toInt() }
    val priority = PriorityQueue<Pair<Long, Int>>(Comparator { a, b ->
        a.first.compareTo(b.first)
    })
    
    for (i in 0 until K) {
        priority.offer(origin[i].toLong() to i)
    }

    for (step in 0 until N) {
        val (now, now_idx) = priority.poll()
        
        if (step == N-1) {
            println(now)
            return
        }
        
        for (idx in 0 until K) {
            val prime = origin[idx]
            val temp = (prime * now).toLong()
            
            if (idx > now_idx) {
                break
            }
            
            priority.offer((temp to idx))
        }
    }
}
