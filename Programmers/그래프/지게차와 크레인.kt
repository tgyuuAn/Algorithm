import java.util.ArrayDeque

class Solution {
    private val dx = intArrayOf(0, 0, -1, 1)
    private val dy = intArrayOf(-1, 1, 0, 0)
    
    fun solution(storage: Array<String>, requests: Array<String>): Int {
        var storage = Array<CharArray>(storage.size+2){ idx ->
            if (idx == 0 || idx == storage.size+1) { 
                CharArray(storage[0].length+2) { '*' } 
            } else { 
                CharArray(storage[0].length+2) { innerIdx ->
                    if (innerIdx == 0 || innerIdx == storage[0].length+1) '*'
                    else storage[idx-1][innerIdx-1] 
                }
            }
        }
        
        // check(storage)
        
        for (request in requests) {
            if (request.length == 1) {
                val request = request.single()
                
                val visited = mutableSetOf<Pair<Int, Int>>()
                visited.add(0 to 0)
                val deq = ArrayDeque<Pair<Int, Int>>()
                deq.addLast(0 to 0)
                
                while (!deq.isEmpty()) {
                    val (nowX, nowY) = deq.removeFirst()
                    
                    for (direction in 0 until 4) {
                        val newX = nowX + dx[direction]
                        val newY = nowY + dy[direction]
                        
                        if (newX < 0 || newX >= storage[0].size) continue
                        if (newY < 0 || newY >= storage.size) continue
                        if (newX to newY in visited) continue
                        
                        if (storage[newY][newX] == '*') {
                            deq.addLast(newX to newY)
                            visited.add(newX to newY)
                            continue
                        }
                        
                        if (storage[newY][newX] == request) {
                            storage[newY][newX] = '*'
                            visited.add(newX to newY)
                            continue
                        }
                    }
                }
            } else {
                val target : Char = request[0]
                
                for (rowIdx in 0 until storage.size) {
                    for (colIdx in 0 until storage[rowIdx].size) {
                        if (storage[rowIdx][colIdx] == target) {
                            storage[rowIdx][colIdx] = '*'
                        }
                    }
                }
            }
        }

        // println()
        // check(storage)
        var answer = 0
        for (rowIdx in 0 until storage.size) {
            for (colIdx in 0 until storage[rowIdx].size) {
                if (storage[rowIdx][colIdx] != '*') {
                    answer += 1
                }
            }
        }
        return answer
    }
    
    // fun check(storage : Array<Array<Char>>) {
    //     for (row in storage) {
    //         for (col in row) {
    //             print(col)
    //         }
    //         println()
    //     }
    // }
}