fun main() {
    val br = System.`in`.bufferedReader()
    val N = br.readLine().toInt()

    val sequence = mutableListOf<Int>()
    repeat(N){
        val elem = br.readLine().toInt()
        sequence.add(elem)
    }
    
    val longSequence = mutableListOf<Int>()
    for (num in sequence) {
        check(num, longSequence)
    }
    
    println(N - longSequence.size)
}

fun check(elem : Int, now : MutableList<Int>) {
    if (now.isEmpty() || elem > now.last()) {
        now.add(elem)
    } else {
        var left = -1
        var right = now.size
        var answer = 0
        
        while (left+1 < right) {
            val mid = (left+right)/2

            if (elem < now[mid]) {
                right = mid
                answer = mid
            } else {
                left = mid
            }
        }
        
        now[answer] = elem
    }
}
