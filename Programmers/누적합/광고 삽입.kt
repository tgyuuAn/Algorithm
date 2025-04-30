class Solution {
    fun solution(play_time: String, adv_time: String, logs: Array<String>): String {
        val playTime = stringTimeToIntTime(play_time)
        val advTime = stringTimeToIntTime(adv_time)
        val allTime = LongArray(100*3600) { 0L }
        
        for (log in logs) {
            val (startTime, endTime) = log.split("-").map { stringTimeToIntTime(it) }
            allTime[startTime] = allTime[startTime] + 1
            allTime[endTime] = allTime[endTime] - 1
        }

        // 각 구간별 시청자수 구하기
        for (idx in 1 until allTime.size) {
            allTime[idx] = allTime[idx-1] + allTime[idx]
        }
        
        // 누적합 구하기
        for (idx in 1 until allTime.size) {
            allTime[idx] = allTime[idx-1] + allTime[idx]
        }
        
        var maxAdvTime : Long = 0L
        var maxDedicate : Int = 0
        for (dedicate in 0..playTime) {
            if (dedicate < advTime) {
                val watchingAdvTime = allTime[dedicate]
                
                if (maxAdvTime < watchingAdvTime) {
                    maxAdvTime = watchingAdvTime
                    maxDedicate = 0
                }
            } else {
                val watchingAdvTime = allTime[dedicate] - allTime[dedicate-advTime]
                
                if (maxAdvTime < watchingAdvTime) {
                    maxAdvTime = watchingAdvTime
                    maxDedicate = dedicate-advTime+1
                }
            }
        }
        
        return intTimeToStringTime(maxDedicate)
    }
    
    fun stringTimeToIntTime(time:String): Int {
        val temp = time.split(":").map { it.toInt() }
        return temp[0] * 3600 + temp[1] * 60 + temp[2]
    }
    
    fun intTimeToStringTime(time: Int): String {
        val hour = (time/3600).toString().padStart(2, '0')
        val minute = ((time%3600)/60).toString().padStart(2, '0')
        val second = (time%60).toString().padStart(2, '0')
        return "${hour}:${minute}:${second}"
    }
}
