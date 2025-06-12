class Solution {
    public int solution(int[] cookies) {
        if (cookies.length == 1) {
            return 0;
        } else if (cookies.length == 2) {
            if (cookies[0] == cookies[1]) {
                return cookies[0];
            } else {
                return 0;
            }
        }
        
        int answer = 0;
        for (int midIdx=1; midIdx<cookies.length; midIdx++) {
            int leftIdx = midIdx-1;
            int rightIdx = midIdx;
            int left = cookies[leftIdx];
            int right = cookies[rightIdx];
            
            while(true) {
                if (left < right) {
                    leftIdx -=1;
                    
                    if (leftIdx <= -1) {
                        break;
                    }

                    left += cookies[leftIdx];
                } else if (left == right) {
                    answer = Math.max(answer, left);
                    
                    if (leftIdx > 0) {
                        leftIdx--;
                        left += cookies[leftIdx];
                    } else if (rightIdx < cookies.length - 1) {
                        rightIdx++;
                        right += cookies[rightIdx];
                    } else {
                        break;
                    }
                } else {
                    rightIdx +=1;
                    
                    if (rightIdx >= cookies.length) {
                        break;
                    }
                    
                    right += cookies[rightIdx];                    
                }
            }
        }
        
        return answer;
    }
}