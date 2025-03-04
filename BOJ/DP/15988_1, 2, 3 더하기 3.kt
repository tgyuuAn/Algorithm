fun main(){
    val T = readln().toInt()
    val DP = Array(1_000_001){ 0L }
    DP[1] = 1
    DP[2] = 2
    DP[3] = 4
    
    for(idx in 4 until 1_000_001) {
        
        var accum : Long = 0L
        for(gap in 1..3) accum += DP[idx-gap] % 1_000_000_009
        DP[idx] = accum % 1_000_000_009
    }
    
    repeat(T) {
        val N = readln().toInt()
        println(DP[N] % 1_000_000_009)
    }
}