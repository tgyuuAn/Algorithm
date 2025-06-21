import java.util.*;
import java.io.*;

class Lamp {
    int pos, w;
    
    public Lamp(int pos, int w) {
        this.pos = pos;
        this.w = w;
    }
    
    @Override
    public String toString() {
        return "pos : " + pos + " w : " + w;
    }
}

class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static List<Lamp> lamps = new ArrayList<Lamp>();
    private static int[] prefixSum;
    private static long[][][] dp;
    private static int N, M;
    
    private static void tokenizing() throws Exception {
        st = new StringTokenizer(br.readLine());
    }
    
    private static int nextInt() {
        return Integer.parseInt(st.nextToken());
    }
    
    public static void main(String[] args) throws Exception {
        tokenizing();
        N = nextInt();
        M = nextInt();
        dp = new long[N+1][N+1][2];
        for (int n=0; n<N+1; n++) {
            for (int m=0; m<N+1; m++) {
                Arrays.fill(dp[n][m], -1);
            }
        }
        
        lamps.add(new Lamp(0, 0));
        prefixSum = new int[N+1];
        int accum = 0;
        for (int i=1; i<N+1; i++) {
            tokenizing();
            int p = nextInt();
            int w = nextInt();
            lamps.add(new Lamp(p, w));
            
            accum += w;
            prefixSum[i] = accum;
        }
        
        System.out.println(recur(M, M, 0));
    }
    
    // direction == 0 이면 왼쪽에 위치, 1이면 오른쪽 위치
    public static long recur(int left, int right, int direction) {
        if (left == 1 && right == N) {
            return 0;
        }
        
        if (dp[left][right][direction] != -1) {
            return dp[left][right][direction];
        }
        
        dp[left][right][direction] = Integer.MAX_VALUE;
        int temp = prefixSum[N] - prefixSum[right] + prefixSum[left-1];
        int cur = (direction == 0) ? left : right;
        // 왼쪽으로 확장
        if (left-1 >= 1) {
            dp[left][right][direction] = recur(left-1, right, 0) + temp * (lamps.get(cur).pos - lamps.get(left-1).pos);
        }
        
        // 오른쪽으로 확장
        if (right+1 <= N) {
            dp[left][right][direction] = Math.min(
                dp[left][right][direction],
                recur(left, right+1, 1) + temp * (lamps.get(right+1).pos - lamps.get(cur).pos)
                );
        }
        
        return dp[left][right][direction];
    }
}