class Solution {
    fun solution(video_len: String, pos: String, op_start: String, op_end: String, commands: Array<String>): String {
        val videoLen = timeToSeconds(video_len)
        var pos = timeToSeconds(pos)
        val opStart = timeToSeconds(op_start)
        val opEnd = timeToSeconds(op_end)
        
        if (pos in opStart..opEnd) {
            pos = opEnd
        }
        
        for (command in commands) {
            when(command) {
                "next" -> {
                    pos = (pos+10).coerceAtMost(videoLen)
                    if (pos in opStart..opEnd) {
                        pos = opEnd
                    }
                }
                "prev" -> {
                    pos = (pos-10).coerceAtLeast(0)
                    if (pos in opStart..opEnd) {
                        pos = opEnd
                    }
                }
            }
        }
        
        return secondsToTime(pos)
    }
    
    fun timeToSeconds(time: String): Int {
        return time.substring(0,2).toInt()*60 + time.substring(3,5).toInt()
    }
    
    fun secondsToTime(seconds: Int): String {
        val minutesString = (seconds/60).toString().padStart(2, '0')
        val secondsString = (seconds%60).toString().padStart(2, '0')
        return "${minutesString}:${secondsString}"
    }
}