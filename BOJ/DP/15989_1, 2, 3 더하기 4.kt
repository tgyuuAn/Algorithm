fun main() {
    val T = readln().toInt()
    
    // DP[i][j] 는 i를 만드는데 마지막 항이 j로 끝나는 수
    val DP = Array(10_001){ Array(4){ 0 } }
    DP[1][1] = 1
    
    DP[2][1] = 1
    DP[2][2] = 1
    
    DP[3][1] = 1
    DP[3][2] = 1
    DP[3][3] = 1
    
    for(idx in 4..10_000) {
        DP[idx][1] = DP[idx-1][1]
        
        DP[idx][2] = DP[idx-2][1] + DP[idx-2][2]
        
        DP[idx][3] = DP[idx-3][1] + DP[idx-3][2] + DP[idx-3][3]
    }
    
    repeat(T) {
        val N = readln().toInt()
        println(DP[N].sum())
    }
}