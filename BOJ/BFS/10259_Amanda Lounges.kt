fun main() {
    val br = System.`in`.bufferedReader()
    val (N, M) = br.readLine().split(" ").map { it.toInt() }
    val hasLounge = HashMap<Int, Boolean?>()
    val graph = HashMap<Int, MutableList<Int>>()

    repeat(N) { idx ->
        hasLounge[idx + 1] = null
    }

    var remainEdges = ArrayDeque<Pair<Int, Int>>()
    repeat(M) {
        val (A, B, C) = br.readLine().split(" ").map { it.toInt() }
        when (C) {
            0 -> {
                if (hasLounge[A] == true || hasLounge[B] == true) {
                    println("impossible")
                    return
                }
                hasLounge[A] = false
                hasLounge[B] = false
            }

            2 -> {
                if (hasLounge[A] == false || hasLounge[B] == false) {
                    println("impossible")
                    return
                }
                hasLounge[A] = true
                hasLounge[B] = true
            }

            1 -> {
                remainEdges.add(A to B)
            }
        }
    }

    var previousCount = 0
    val temp = ArrayDeque<Pair<Int, Int>>()
    while (previousCount != remainEdges.size) {
        for ((a, b) in remainEdges) {
            val aVal = hasLounge[a]
            val bVal = hasLounge[b]

            if (aVal == null && bVal == null) {
                temp.add(a to b)
                continue
            }

            if (aVal == true && bVal == true || aVal == false && bVal == false) {
                println("impossible")
                return
            }

            if (aVal == true && bVal == null) {
                hasLounge[b] = false
            } else if (aVal == null && bVal == true) {
                hasLounge[a] = false
            } else if (aVal == false && bVal == null) {
                hasLounge[b] = true
            } else if (aVal == null && bVal == false) {
                hasLounge[a] = true
            }
        }

        if (temp.isEmpty()) {
            val answer = hasLounge.count { it.value == true }
            println(answer)
            return
        }

        previousCount = remainEdges.size
        remainEdges = ArrayDeque(temp)
        temp.clear()
    }

    // 이제 남은 것들로 이분 그래프 탐색
    for ((a, b) in remainEdges) {
        graph.computeIfAbsent(a) { mutableListOf() }.add(b)
        graph.computeIfAbsent(b) { mutableListOf() }.add(a)
    }

    val color = HashMap<Int, Int>() // 0 or 1
    var answer = hasLounge.count { it.value == true }

    for ((node, _) in graph) {
        if (color.containsKey(node)) continue

        val queue = ArrayDeque<Int>()
        queue.add(node)
        color[node] = 0
        var count0 = 0
        var count1 = 0
        var valid = true

        while (queue.isNotEmpty()) {
            val cur = queue.removeFirst()
            val c = color[cur]!!
            if (hasLounge[cur] != null) {
                if ((hasLounge[cur] == true && c != 1) || (hasLounge[cur] == false && c != 0)) {
                    println("impossible")
                    return
                }
            }
            if (c == 0) count0++ else count1++

            for (next in graph[cur] ?: emptyList()) {
                if (!color.containsKey(next)) {
                    color[next] = 1 - c
                    queue.add(next)
                } else if (color[next] == c) {
                    println("impossible")
                    return
                }
            }
        }

        answer += minOf(count0, count1)
    }

    println(answer)
}