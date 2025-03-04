fun main(){
    val (N, K) = readln().split(" ")
        .map{ it.toInt() }
    
    val DP = Array(12){ mutableListOf<String>() }
    DP[1] = mutableListOf("1")
    DP[2] = mutableListOf("1+1", "2")
    DP[3] = mutableListOf("1+1+1", "2+1", "1+2", "3")
    
    for(idx in 4..N) {
        for(gap in 1..3) {
            for(previous in DP[idx-gap]) {
                DP[idx].add("${previous}+${gap}")
            }
        }
    }
    
    if(DP[N].size < K) {
        print("-1")
    } else {
        print(DP[N].sorted()[K-1])
    }
}