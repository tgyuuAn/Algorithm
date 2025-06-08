class Solution {
    public int solution(int sticker[]) {
        int answer = 0;
        
        if (sticker.length == 1) {
            return sticker[0];
        }
        
        // 첫 항을 뗐을 때,
        int[][] dp = new int[sticker.length+1][2];
        dp[1][0] = sticker[0];
        
        for (int idx=1; idx<=sticker.length; idx++) {
            int curVal = sticker[idx-1];
            
            dp[idx][0] = dp[idx-1][1] + curVal;
            dp[idx][1] = Math.max(dp[idx-1][0], dp[idx-1][1]);
        }
        
        // 첫 항을 떼지 않았을 때,
        int[][] dp2 = new int[sticker.length+1][2];
        for (int idx=2; idx<=sticker.length; idx++) {
            int curVal = sticker[idx-1];
            
            dp2[idx][0] = dp2[idx-1][1] + curVal;
            dp2[idx][1] = Math.max(dp2[idx-1][0], dp2[idx-1][1]);
        }
        
        return Math.max(
            Math.max(dp[sticker.length-1][0], dp[sticker.length-1][1]),
            Math.max(dp2[sticker.length][0], dp2[sticker.length][1])
        );
    }
}