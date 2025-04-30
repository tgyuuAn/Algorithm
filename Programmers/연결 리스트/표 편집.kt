class Solution {
    fun solution(n: Int, k: Int, cmd: Array<String>): String {
        val sb = StringBuilder()
        var currentIdx = k
        val removeStack = mutableListOf<Int>()
        val tableState = BooleanArray(n){ true }
        val linkedList = MutableList<Pair<Int?, Int?>>(n) { idx ->
            val prev: Int? = if (idx-1 >=0) idx-1 else null
            val next: Int?= if (idx+1 < n) idx+1 else null
            prev to next
        }
        
        for (c in cmd) {
            when(c[0]) {
                'D' -> {
                    val count = c.substring(2, c.length).toInt()
                    
                    repeat(count) {
                        do {
                            val next = linkedList[currentIdx].second
                            if (next != null) currentIdx = next
                        } while (tableState[currentIdx] != true)
                    }
                }
                
                'U' -> {
                    val count = c.substring(2, c.length).toInt()
                    
                    repeat(count) {
                        do {
                            val prev = linkedList[currentIdx].first
                            if (prev != null) currentIdx = prev
                        } while (tableState[currentIdx] != true)
                    }
                }
                
                'C' -> {
                    tableState[currentIdx] = false
                    removeStack.add(currentIdx)
                    
                    val (prev, next) = linkedList[currentIdx]
                    if (prev != null) {
                        linkedList[prev] = linkedList[prev].first to next
                    }
                    
                    if (next != null) {
                        linkedList[next] = prev to linkedList[next].second
                    }
                    
                    var tempIdx: Int? = currentIdx
                    while (tempIdx != null && tableState[tempIdx] == false) {
                        val next = linkedList[tempIdx!!].second
                        tempIdx = next
                    }
                    
                    if (tempIdx != null) {
                        currentIdx = tempIdx!!
                    } else {
                        tempIdx = currentIdx
                        while(tempIdx != null && tableState[tempIdx] == false) {
                            val prev = linkedList[tempIdx].first
                            tempIdx = prev
                        }
                        currentIdx = tempIdx!!
                    }
                }
                'Z' -> {
                    if (!removeStack.isEmpty()) {
                        val restoreIdx = removeStack.removeLast()
                        tableState[restoreIdx] = true
                        
                        var prev = linkedList[restoreIdx].first
                        var next = linkedList[restoreIdx].second
                        if (prev != null) {
                            linkedList[prev] = linkedList[prev].first to restoreIdx
                        }
                        
                        if (next != null) {
                            linkedList[next] = restoreIdx to linkedList[next].second
                        }
                        
                        linkedList[restoreIdx] = prev to next
                    }
                }
            }
        }
        
        for (state in tableState) {
            if (state == true) sb.append("O")
            else sb.append("X")
        }
        
        return sb.toString()
    }
}