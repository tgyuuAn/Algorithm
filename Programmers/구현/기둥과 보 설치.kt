import java.util.*

class Solution {
    private val building = mutableSetOf<Triple<Int, Int, Int>>()
    private val dx = intArrayOf(0, 0, -1, 1)
    private val dy = intArrayOf(-1, 1, 0, 0)
    
    fun solution(n: Int, build_frame: Array<IntArray>): Array<IntArray> {        
        for (command in build_frame) {
            val (x, y, type, method) = command
            // println("commnad $x $y $type $method")
            
            when (method) {
                DESTROY -> {
                    if (Triple(x, y, type) in building) {
                        building.remove(Triple(x, y, type))     
                        
                        if (check()==false) {
                            building.add(Triple(x, y, type))                            
                        }
                    }
                }
                
                BUILD -> {
                    building.add(Triple(x, y, type))     
                        
                    if (check()==false) {
                        building.remove(Triple(x, y, type))                            
                    }
                }
            }
            
            // println()
            // println(building)
        }

        var answer: Array<IntArray> = building.toList()
            .sortedWith ( compareBy( { it. first }, { it.second }, { it.third } ) )
            .map { intArrayOf(it.first, it.second, it.third) }
            .toTypedArray()
            
        return answer
    }
    
    fun check(): Boolean {
        val visited = mutableSetOf<Triple<Int, Int, Int>>()
        
        for (node in building) {
            if (node in visited) continue
    
            val deque = ArrayDeque<Triple<Int, Int, Int>>()
            deque.addLast(node)
            
            while (!deque.isEmpty()) {
                val now = deque.removeFirst()
                val nowX = now.first
                val nowY = now.second
                val type = now.third
                
                // 현재 타입이 가능한 건축물인지 확인
                when(type) {
                    PILLAR -> {
                        var isSafe = false
                        
                        if (nowY == 0) { // 바닥 위
                            isSafe = true
                        } else if (Triple(nowX, nowY-1, PILLAR) in building) { // 바로 아래쪽에 기둥
                            isSafe = true
                        } else if (Triple(nowX-1, nowY, RUG) in building) { // 왼쪽 -> 오른쪽으로 보가 있음
                            isSafe = true
                        } else if (Triple(nowX, nowY, RUG) in building) { // 오른쪽 -> 왼쪽으로 보가 있음
                            isSafe = true
                        }
                        
                        if(!isSafe) return false
                    }
                
                    RUG -> {
                        // 보는 한쪽 끝 부분이 기둥 위에 있거나, 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 함
                        var isSafe = false
                        
                        if (Triple(nowX, nowY-1, PILLAR) in building) { // 왼쪽 끝이 기둥 위에 존재
                            isSafe = true
                        } else if (Triple(nowX+1, nowY-1, PILLAR) in building) { // 오른쪽 끝이 기둥 위에 존재
                            isSafe = true
                        } else if (Triple(nowX-1, nowY, RUG) in building && Triple(nowX+1, nowY, RUG) in building) { // 양쪽이 보로 연결
                            isSafe = true
                        }
                        
                        if(!isSafe) return false
                    }
                }
                
                // 연결된 건축물을 Deque에 넣음
                when (type) {
                    PILLAR -> {
                        // 위쪽(왼->오)에 있는 보
                        if (Triple(nowX-1, nowY+1, RUG) in building && Triple(nowX-1, nowY+1, RUG) !in visited) {
                            visited.add(Triple(nowX-1, nowY+1, RUG))
                            deque.addLast(Triple(nowX-1, nowY+1, RUG))
                        }
                        
                        // 위쪽(오->왼)에 있는 보
                        if (Triple(nowX, nowY+1, RUG) in building && Triple(nowX, nowY+1, RUG) !in visited) {
                            visited.add(Triple(nowX, nowY+1, RUG))
                            deque.addLast(Triple(nowX, nowY+1, RUG))
                        }
                        
                        // 아래쪽(왼->오)에 있는 보
                        if (Triple(nowX-1, nowY, RUG) in building && Triple(nowX-1, nowY, RUG) !in visited) {
                            visited.add(Triple(nowX-1, nowY, RUG))
                            deque.addLast(Triple(nowX-1, nowY, RUG))
                        }
                        
                        // 아래쪽(오->왼)에 있는 보
                        if (Triple(nowX, nowY, RUG) in building && Triple(nowX, nowY, RUG) !in visited) {
                            visited.add(Triple(nowX, nowY, RUG))
                            deque.addLast(Triple(nowX, nowY, RUG))
                        }
                        
                        // 위쪽에 있는 기둥
                        if (Triple(nowX, nowY+1, PILLAR) in building && Triple(nowX, nowY+1, PILLAR) !in visited) {
                            visited.add(Triple(nowX, nowY+1, PILLAR))
                            deque.addLast(Triple(nowX, nowY+1, PILLAR))
                        }
                        
                        // 아래쪽에 있는 기둥
                        if (Triple(nowX, nowY-1, PILLAR) in building && Triple(nowX, nowY-1, PILLAR) !in visited) {
                            visited.add(Triple(nowX, nowY-1, PILLAR))
                            deque.addLast(Triple(nowX, nowY-1, PILLAR))
                        }
                    }
                    
                    RUG -> {
                        // 왼쪽 밑에 있는 기둥
                        if (Triple(nowX, nowY-1, PILLAR) in building && Triple(nowX, nowY-1, PILLAR) !in visited) {
                            visited.add(Triple(nowX, nowY-1, PILLAR))
                            deque.addLast(Triple(nowX, nowY-1, PILLAR))
                        }
                        
                        // 오른쪽 밑에 있는 기둥
                        if (Triple(nowX+1, nowY-1, PILLAR) in building && Triple(nowX+1, nowY-1, PILLAR) !in visited) {
                            visited.add(Triple(nowX+1, nowY-1, PILLAR))
                            deque.addLast(Triple(nowX+1, nowY-1, PILLAR))
                        }
                        
                        // 왼쪽 위에 있는 기둥
                        if (Triple(nowX, nowY, PILLAR) in building && Triple(nowX, nowY, PILLAR) !in visited) {
                            visited.add(Triple(nowX, nowY, PILLAR))
                            deque.addLast(Triple(nowX, nowY, PILLAR))
                        }
                        
                        // 오른쪽 위에 있는 기둥
                        if (Triple(nowX+1, nowY, PILLAR) in building && Triple(nowX+1, nowY, PILLAR) !in visited) {
                            visited.add(Triple(nowX+1, nowY, PILLAR))
                            deque.addLast(Triple(nowX+1, nowY, PILLAR))
                        }
                        
                        // 오른쪽에 있는 보
                        if (Triple(nowX+1, nowY, RUG) in building && Triple(nowX+1, nowY, RUG) !in visited) {
                            visited.add(Triple(nowX+1, nowY, RUG))
                            deque.addLast(Triple(nowX+1, nowY, RUG))
                        }
                        
                        // 왼쪽에 있는 보
                        if (Triple(nowX-1, nowY, RUG) in building && Triple(nowX-1, nowY, RUG) !in visited) {
                            visited.add(Triple(nowX-1, nowY, RUG))
                            deque.addLast(Triple(nowX-1, nowY, RUG))
                        }
                    }
                }
            }
        }
        
        return true
    }
    
    companion object {
        private const val PILLAR = 0
        private const val RUG = 1
        private const val DESTROY = 0
        private const val BUILD = 1 
    }
}