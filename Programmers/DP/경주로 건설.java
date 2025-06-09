import java.util.PriorityQueue;
import java.util.Arrays;

class Node implements Comparable<Node> {
    final static int LEFT = 0;
    final static int RIGHT = 1;
    final static int UP = 2;
    final static int DOWN = 3;
    
    int prevDirection;
    int row;
    int col;
    int cost;
    
    public Node(int row, int col, int cost, int prevDirection) {
        this.row = row;
        this.col = col;
        this.cost = cost;        
        this.prevDirection = prevDirection;
    }
    
    public boolean isStraight(int newRow, int newCol) {
        if ((prevDirection == UP || prevDirection == DOWN) && this.col != newCol) {
            return false;
        }
        
        if ((prevDirection == LEFT || prevDirection == RIGHT) && this.row != newRow) {
            return false;
        }
        
        return true;
    }
    
    @Override
    public int compareTo(Node other) {
        return this.cost - other.cost;
    }
}

class Solution {
    private int[][][] costBoard;

    private int[] dx = { -1, 1, 0, 0 };
    private int[] dy = { 0, 0, -1, 1 };
    private static final int STRAIGHT_COST = 100;
    private static final int CORNER_COST = 500;
    
    private int rowLength;
    private int colLength;
    
    public int solution(int[][] board) {
        rowLength = board.length;
        colLength = board[0].length;
        
        costBoard = new int[rowLength][colLength][4];        
        for (int[][] costRow : costBoard) {
            for (int[] costCol : costRow) {
                Arrays.fill(costCol, Integer.MAX_VALUE);
            }
        }
        
        PriorityQueue<Node> pq = new PriorityQueue<Node>();
        for (int dir=0; dir<4; dir++){
            pq.offer(new Node(0, 0, 0, dir));
        }
        
        while(!pq.isEmpty()) {
            Node curNode = pq.poll();
            
            if (costBoard[curNode.row][curNode.col][curNode.prevDirection] > curNode.cost) {
                costBoard[curNode.row][curNode.col][curNode.prevDirection] = curNode.cost;
            }
            
            // testPrint();
            
            for (int dir=0; dir<4; dir++) {
                int newRow = curNode.row + dy[dir];
                int newCol = curNode.col + dx[dir];
                
                if (newRow < 0 || newRow >= rowLength) {
                    continue;
                }
                
                if (newCol < 0 || newCol >= colLength) {
                    continue;
                }
                
                if (board[newRow][newCol] == 1) {
                    continue;
                }
                
                if (curNode.isStraight(newRow, newCol)) {
                    // 직선 길일 경우
                    int newCost = curNode.cost + STRAIGHT_COST;
                    
                    if (costBoard[newRow][newCol][dir] < newCost) {
                        continue;
                    }
                    
                    pq.offer(new Node(newRow, newCol, newCost, dir));               
                } else {
                    // 코너 길일 경우
                    int newCost = curNode.cost + CORNER_COST + STRAIGHT_COST;
                    
                    if (costBoard[newRow][newCol][dir] < newCost) {
                        continue;
                    }
                    
                    pq.offer(new Node(newRow, newCol, newCost, dir));             
                }
            }
        }
        
        int answer = Integer.MAX_VALUE;
        for (int cost : costBoard[rowLength-1][colLength-1]){
            answer = Math.min(answer, cost);
        }
        
        return answer;
    }
    
    private void testPrint() {
        for (int[][] tempRow : costBoard) {
            for (int[] temp : tempRow) {
                System.out.println(Arrays.toString(temp));
            }
        }
        System.out.println();
    }
}