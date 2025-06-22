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
        if (N<=2) {
            System.out.println(N);
            return;
        }
        
        int[] dp = new int[N+1];
        dp[1] = 1;
        dp[2] = 2;
        
        for (int i=3; i<N+1; i++) {
            dp[i] = dp[i-1] % 10_007 + dp[i-2] % 10_007;
            dp[i] %= 10_007;
        }
        
        System.out.println(dp[N]);
    }
}