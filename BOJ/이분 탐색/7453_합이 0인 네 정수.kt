import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val N = br.readLine().toInt()
    val A = IntArray(N)
    val B = IntArray(N)
    val C = IntArray(N)
    val D = IntArray(N)
    
    for (i in 0 until N) {
        val st = StringTokenizer(br.readLine())
        A[i] = st.nextToken().toInt()
        B[i] = st.nextToken().toInt()
        C[i] = st.nextToken().toInt()
        D[i] = st.nextToken().toInt()
    }
    
    val CD = IntArray(N * N)
    var idx = 0
    for (i in 0 until N) {
        for (j in 0 until N) {
            CD[idx++] = C[i] + D[j]
        }
    }
    
    CD.sort()
    
    var ans: Long = 0
    for (i in 0 until N) {
        for (j in 0 until N) {
            val temp = A[i] + B[j]
            val upper = upperBound(-temp, CD)
            val lower = lowerBound(-temp, CD)
            ans += (upper - lower)
        }
    }
    println(ans)
}

fun upperBound(key: Int, arr: IntArray): Int {
    var start = 0
    var end = arr.size - 1
    while (start <= end) {
        val mid = (start + end) / 2
        if (arr[mid] > key) {
            end = mid - 1
        } else {
            start = mid + 1
        }
    }
    return start
}

fun lowerBound(key: Int, arr: IntArray): Int {
    var start = 0
    var end = arr.size - 1
    while (start <= end) {
        val mid = (start + end) / 2
        if (arr[mid] >= key) {
            end = mid - 1
        } else {
            start = mid + 1
        }
    }
    return start
}
