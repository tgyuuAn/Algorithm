import java.util.*;
import java.io.*;

class Crime {
    int R, C;
        
    public Crime (int R, int C) {
        this.R = R;
        this.C = C;
    }
    
    @Override
    public String toString() {
        return "R : "+ R + " C : " + C;
    }
}
    
class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static int N, W;
    private static List<Crime> crimes = new ArrayList<Crime>();
    private static int[][] dp;
    private static int[] allocated;
    
    private static void tokenizing() throws Exception {
        st = new StringTokenizer(br.readLine());
    }
    
    private static int nextInt() {
        return Integer.parseInt(st.nextToken());
    }

    public static void main(String[] args) throws Exception {
        tokenizing();
        N = nextInt();
        tokenizing();
        W = nextInt();
        
        crimes.add(new Crime(0, 0));        
        for (int i=0; i<W; i++){
            tokenizing();
            int R = nextInt();
            int C = nextInt();
            crimes.add(new Crime(R, C));
        }
        
        dp = new int[W+1][W+1];
        allocated = new int[W+1];
        for (int idx=0; idx<W+1; idx++) {
            Arrays.fill(dp[idx], -1);
        }
        
        System.out.println(recur(0, 0));
        trace(0, 0);
        for (int idx=1; idx<W+1; idx++) {
            System.out.println(allocated[idx]);
        }
    }
    
    private static int recur(int a, int b) {
        if (a == W || b == W) {
            return 0;
        }
        
        if (dp[a][b] != -1) {
            return dp[a][b];
        }
        
        int next = Math.max(a, b) + 1;
        int aCost = recur(next, b) + dist(a, next);
        int bCost = recur(a, next) + dist(next, b);
        if (aCost <= bCost) {
            dp[a][b] = aCost;
        } else {
            dp[a][b] = bCost;
        }
        
        return dp[a][b];
    }
    
    private static int dist(int a, int b) {
        if (a==0) {
            return crimes.get(b).R-1 + crimes.get(b).C-1;
        }
        
        if (b==0) {
            return (N - crimes.get(a).R) + (N - crimes.get(a).C);
        }
        
        Crime aCrime = crimes.get(a);
        Crime bCrime = crimes.get(b);
        return Math.abs(aCrime.R - bCrime.R) + Math.abs(aCrime.C - bCrime.C);
    }
    
    private static void trace(int a, int b) {
        if (Math.max(a, b) == W) return;

        int next = Math.max(a, b) + 1;
        int aCost = recur(next, b) + dist(a, next);
        int bCost = recur(a, next) + dist(next, b);

        if (aCost <= bCost) {
            allocated[next] = 1;
            trace(next, b);
        } else {
            allocated[next] = 2;
            trace(a, next);
        }
    }
}
