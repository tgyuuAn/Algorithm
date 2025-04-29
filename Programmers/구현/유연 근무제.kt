class Solution {
    fun solution(schedules: IntArray, timelogs: Array<IntArray>, startday: Int): Int {
        var answer: Int = 0
        schedules.zip(timelogs) { schedule, timelog -> 
            val scheduleMinute = timeToMinute(schedule)
            var isGift = true
            for (idx in 0 until timelog.size) {
                if ((idx + startday)%7 in setOf(0,6)) continue
                
                val intoTime = timeToMinute(timelog[idx])
                if (intoTime > scheduleMinute+10) {
                    isGift = false
                    break
                }
            }
            
            if (isGift) {
                answer += 1
            }
        }
        
        return answer
    }
    
    fun timeToMinute(time:Int):Int {
        return (time/100)*60+time%100
    }
}