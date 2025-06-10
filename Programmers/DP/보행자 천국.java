import java.util.*;

class Node {
    int row;
    int col;
    int cost;
    int dir;
    
    public Node(int row, int col, int cost, int dir) {
        this.row = row;
        this.col = col;
        this.cost = cost;
        this.dir = dir;
    }
    
    @Override
    public String toString() {
        return String.format("Node \n row : %d \n col : %d \n cost : %d \n dir : %d", row, col, cost, dir);
    }
}

class Solution {
    int MOD = 20170805;
    private static final int[] dx = { 0, 1 };
    private static final int[] dy = { 1, 0 };
    
    public int solution(int m, int n, int[][] cityMap) {
        int[][][] dp = new int[m][n][2];
        int[][][] cost = new int[m][n][2];
        
        for (int[][] costRow : cost) {
            for (int[] costCol : costRow) {
                Arrays.fill(costCol, Integer.MAX_VALUE);
            }
        }
        dp[0][0][0] = 1;
        dp[0][0][1] = 1;
        
        cost[0][0][1] = 0;
        cost[0][0][1] = 0;
        
        ArrayDeque<Node> deq = new ArrayDeque<Node>();
        deq.add(new Node(0,0,0,0));
        deq.add(new Node(0,0,0,1));
        while (!deq.isEmpty()) {
            Node curNode = deq.removeFirst();
            
            for (int dir=0; dir<2; dir++) {
                int newRow = curNode.row + dy[dir];
                int newCol = curNode.col + dx[dir];
                int newCost = curNode.cost+1;
                
                if (newRow >= m || newCol >= n) {
                    continue;
                }
                
                int originCost = cost[newRow][newCol][dir];
                if (originCost < newCost) {
                    continue;
                }
                
                if (originCost > newCost) {
                    if (cityMap[newRow][newCol] == 1) {
                        continue;
                    }
                    
                    if (cityMap[curNode.row][curNode.col] == 2 && curNode.dir != dir) {
                        continue;
                    }
                    
                    if ((curNode.row==0 && curNode.col==0) ||
                        (cityMap[curNode.row][curNode.col] == 2 && curNode.dir == dir)) {          
                        dp[newRow][newCol][dir] += dp[curNode.row][curNode.col][curNode.dir] % MOD;
                        dp[newRow][newCol][dir] %= MOD;
                        cost[newRow][newCol][dir] = newCost;
                        deq.add(new Node(newRow, newCol, newCost, dir));
                        continue;
                    }
                    
                    dp[newRow][newCol][dir] += dp[curNode.row][curNode.col][0] % MOD;
                    dp[newRow][newCol][dir] += dp[curNode.row][curNode.col][1] % MOD;
                    dp[newRow][newCol][dir] %= MOD;
                    cost[newRow][newCol][dir] = newCost;
                    deq.add(new Node(newRow, newCol, newCost, dir));
                }
            }
        }
        
        return (dp[m-1][n-1][0] + dp[m-1][n-1][1]) % MOD;
    }
}