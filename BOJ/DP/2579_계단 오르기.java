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
        int[] stairs = new int[N+1];
        for (int step=1; step<N+1; step++) {
            tokenizing();
            int M = nextInt();
            stairs[step] = M;
        }
        
        if (N==1) {
            System.out.println(stairs[1]);
            return;
        }
        
        int[][] dp = new int[N+1][2];
        dp[1][0] = stairs[1];
        dp[2][0] = stairs[2];
        
        for (int step=1; step<N+1; step++) {
            for (int value : dp[step]) {
                // 두개 한꺼번에 건너기
                if (step+2<=N) {
                    dp[step+2][0] = Math.max(dp[step+2][0], value + stairs[step+2]);
                }
            }
            
            // 하나씩 건너기
            if (step+1<=N) {
                dp[step+1][1] = Math.max(dp[step+1][1], dp[step][0] + stairs[step+1]);
            }
        }
        
        int answer = Math.max(dp[N][0], dp[N][1]);
        System.out.println(answer);
    }
}