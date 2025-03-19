fun main() {
    val N = readln().toInt()
    val sequence = readln().split(" ").map{ it.toInt() }
    var answer : Long = 0L
    
    var right = 0
    var left = 0
    val tempSet = mutableSetOf<Int>()
    while (left <= right) {
        tempSet.add(sequence[right])

        if (tempSet.size == (right-left)+1) {      // 중복이 없을 경우
            if (right < sequence.size-1) {         // right가 마지막 인덱스가 아닐 경우
                right += 1
            } else {                               // right가 마지막 인덱스일 경우
                answer += (right-left)+1
                
                if (sequence[right] != sequence[left]) tempSet.remove(sequence[left])
                left += 1
            }
            
            continue
        }
                                                   // 중복이 있을 경우
        answer += (right-left)
        
        if (sequence[right] != sequence[left]) tempSet.remove(sequence[left])
        left += 1
    }
    
    println(answer)
}