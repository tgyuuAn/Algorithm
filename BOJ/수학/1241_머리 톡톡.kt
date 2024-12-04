import kotlin.math.*;

fun main() {
    val N = readln().toInt()
    val answer = HashMap<Int, Int>()
    val counter = HashMap<Int, Int>()
    val numbers = mutableListOf<Int>()
    val forCheck = mutableSetOf<Int>()
    
    repeat(N) { idx ->
        val now = readln().toInt()
        counter[now] = (counter[now] ?: 0) + 1
        numbers.add(now)
        forCheck.add(now)
    }
    
    for(number in numbers) {
        if(answer[number] == null) {
            for(i in 1 until (sqrt(number.toFloat()).toInt()+1)) {
                if(number%i==0) {
                    answer[number] = (answer[number]?:0) + (counter[i] ?: 0)
                
                    if(i != number/i){
                        answer[number] = (answer[number]?:0) + (counter[number/i] ?: 0)
                    }
                }
            }
        }
        
        println((answer[number]?:1)-1)
    }
}
