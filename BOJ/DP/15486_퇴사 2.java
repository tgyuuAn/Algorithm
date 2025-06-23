import java.util.*;
import java.io.*;

class Main {
    private static int[][] counsels;
    private static int N;
    
    private static void setUp() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        counsels = new int[N+1][2];
        for (int i=1; i<N+1; i++) {
            st = new StringTokenizer(br.readLine());
            int T = Integer.parseInt(st.nextToken());
            int P = Integer.parseInt(st.nextToken());
            counsels[i] = new int[] { T, P };
        }
    }
    
    public static void main(String[] args) throws Exception {
        setUp();
        
        int[] dp = new int[N+2];
        for (int cur=1; cur<N+1; cur++) {
            int[] curCounsel = counsels[cur];
            
            dp[cur] = Math.max(dp[cur], dp[cur-1]);
            if (cur + curCounsel[0] < N+2) {
                dp[cur + curCounsel[0]] = Math.max(dp[cur + curCounsel[0]], dp[cur]+curCounsel[1]);
            }
        }
        
        dp[N+1] = Math.max(dp[N+1], dp[N]);
        System.out.println(dp[N+1]);
    }
}