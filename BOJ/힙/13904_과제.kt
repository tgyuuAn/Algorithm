import java.util.*
import kotlin.math.*

fun main() {
    val br = System.`in`.bufferedReader()
    val N = br.readLine().toInt()
    val heap = PriorityQueue<Pair<Int, Int>>(Comparator { a, b ->
        val cmpFirst = b.second.compareTo(a.second)
        
        if (cmpFirst != 0) {
            cmpFirst
        } else {
            a.first.compareTo(b.first)
        }
    })
    
    repeat(N) {
        val (d, w) = br.readLine().split(" ").map{ it.toInt() }
        heap.offer(d to w)
    }
    
    val board = HashMap<Int, Int>()
    while (!heap.isEmpty()) {
        val (remain_day, score) = heap.poll()
        
        var search_day = remain_day
        while(board[search_day] != null) {
            search_day -= 1
        }
        
        if (search_day < 1) continue
        
        board[search_day] = score
    }
    
    println(board.values.sum())
}
