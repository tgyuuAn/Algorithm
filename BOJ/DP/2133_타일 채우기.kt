fun main() {
    val br = System.`in`.bufferedReader()
    val N = br.readLine().toInt()
    
    if (N%2==1) { 
        println(0)
        return
    }
    
    val dpTable = IntArray(N+1) { 0 }
    dpTable[0] = 1
    dpTable[2] = 3

    for (idx in 4..N step(2)) {
        dpTable[idx] = dpTable[idx-2]*3
        
        for (inner_idx in 0..idx-4 step(2)) {
            dpTable[idx] += dpTable[inner_idx]*2
        }
    }
    
    println(dpTable[N])
}

// https://yabmoons.tistory.com/536