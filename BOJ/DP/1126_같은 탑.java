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
        
        tokenizing();
        int accum = 0;
        List<Integer> elements = new ArrayList<Integer>();
        for (int i=0; i<N; i++) {
            int elem = nextInt();
            accum += elem;
            elements.add(elem);
        }
        
        int[] dp = new int[accum+1];
        for (int i=0; i<accum+1; i++) {
            dp[i] = -1;
        }
        dp[0] = 0;

        for (int i=0; i<N; i++) {
            Integer curHeight = elements.get(i);
            int[] next = Arrays.copyOf(dp, dp.length);
            
            for (int diff=0; diff<accum+1; diff++) {
                if(dp[diff] == -1) {
                    continue;
                }
            
                if (diff+curHeight <= accum) {
                    next[diff+curHeight] = Math.max(next[diff+curHeight], dp[diff]);
                }
                
                int newDiff = Math.abs(curHeight-diff);
                int addedHeight = Math.min(curHeight, diff);
                next[newDiff] = Math.max(next[newDiff], dp[diff] + addedHeight);
            }
            
            dp = next;
        }
        
        System.out.println(dp[0] == 0 ? -1 : dp[0]);
    }
}