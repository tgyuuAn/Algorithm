import java.util.ArrayDeque
import kotlin.math.*

class Solution {
    fun solution(players: IntArray, m: Int, k: Int): Int {
        var answer: Int = 0
        var nowServer = 1
        var serverDeque = ArrayDeque<Pair<Int,Int>>()
        
        for (hour in 0 until players.size) {
            while(!serverDeque.isEmpty() && serverDeque.first.second <= hour) {
                val (poppedServerAmount, _) = serverDeque.removeFirst()
                nowServer -= poppedServerAmount
            }

            val nowPlayers = players[hour]
            if (nowPlayers >= nowServer*m) {
                val needServerAmount = floor(nowPlayers.toDouble()/m).toInt()-nowServer+1
                serverDeque.addLast((needServerAmount to hour+k))
                nowServer += needServerAmount
                answer += needServerAmount
            }
        }
        
        return answer
    }
}