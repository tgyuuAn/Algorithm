import kotlin.math.*;

fun main() {
    val br = System.`in`.bufferedReader()
    val (N, K) = br.readLine()
                .split(" ")
                .map{ it.toInt() }
    
    val sequence = mutableListOf<Int>()
    repeat(N) {
        val num = br.readLine().toInt()
        sequence.add(num)
    }
    sequence.sort()
    
    val dpTable = IntArray(K+1){ -1 }
    dpTable[0] = 0
    for (elem in sequence) {
        for (now in 0..K-elem) {
            if(dpTable[now] != -1){
                if (dpTable[now+elem] == -1) {
                    dpTable[now+elem] = dpTable[now]+1
                } else {
                    dpTable[now+elem] = min(dpTable[now]+1, dpTable[now+elem])
                }
            }
        }
    }
    
    print(dpTable[K])
}
