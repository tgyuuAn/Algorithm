import java.util.*;
import java.io.*;

class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    
    private static void tokenizing() throws Exception {
        st = new StringTokenizer(br.readLine());
    }
    
    private static int nextInt() {
        return Integer.parseInt(st.nextToken());
    }
    
    public static void main(String[] args) throws Exception {
        tokenizing();
        int N = nextInt();
        int[] dp = new int[N+1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[N] = 0;
        
        for (int step=N; step>0; step--) {
            if (step%3==0) {
                dp[step/3] = Math.min(dp[step/3], dp[step]+1);
            }
            
            if (step%2==0) {
                dp[step/2] = Math.min(dp[step/2], dp[step]+1);
            }
            
            if (step>0) {
                dp[step-1] = Math.min(dp[step-1], dp[step]+1);
            }
        }
        
        System.out.println(dp[1]);
    }
}