class Solution {
    private static final int DIV = 1_000_000_007;
    
    public int solution(int n, int[] money) {
        int answer = 0;
        int[] dp = new int[n+1];
        dp[0] = 1;
        
        for (int curMoney : money) {
            for (int curIdx=curMoney; curIdx<=n; curIdx++) {
                dp[curIdx] += dp[curIdx-curMoney]%DIV;
                dp[curIdx] %= DIV;
            }
        }
        
        return dp[n]%DIV;
    }
}