val MIN_VALUE = -1_000_000_001

fun main() {
    val br = System.`in`.bufferedReader()
    val N = br.readLine().toInt()
    val lines = mutableListOf<Pair<Int, Int>>()
    repeat(N){
        val arr = br.readLine().split(" ").map{ it.toInt() }
        lines.add(arr[0] to arr[1])
    }
    lines.sortWith(compareBy({ it.first }, { it.second }))
    
    var answer = 0
    var previousStart = MIN_VALUE
    var previousEnd = MIN_VALUE
    for(line in lines){
        val nowStart = line.first
        val nowEnd = line.second

        if(previousStart == MIN_VALUE){
            previousStart = nowStart
            previousEnd = nowEnd
            answer += previousEnd - previousStart
            continue
        }
        
        if(previousEnd <= nowStart){
            previousStart = nowStart
            previousEnd = nowEnd
            answer += previousEnd - previousStart
            continue
        }
        
        if(nowStart < previousEnd){
            if(nowEnd < previousEnd){
                continue
            }
            
            answer += nowEnd - previousEnd
            previousEnd = nowEnd
            continue
        }
    }

    print(answer)
}
