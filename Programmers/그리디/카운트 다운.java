import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;
import java.util.PriorityQueue;

class Target {
    int score;
    boolean isSingleOrBull;
    
    public Target(int score, boolean isSingleOrBull) {
        this.score = score;
        this.isSingleOrBull = isSingleOrBull;
    }
    
    @Override
    public String toString() {
        return "Score : " + score + ", isSingleOrBull : " + isSingleOrBull;
    }
}

class Node implements Comparable<Node> {
    int score;
    int totCnt;
    int singleOrBullCnt;
    
    public Node(int score, int totCnt, int singleOrBullCnt) {
        this.score = score;
        this.totCnt = totCnt;
        this.singleOrBullCnt = singleOrBullCnt;
    }
    
    @Override
    public int compareTo(Node other) {
        int firstCmp = this.totCnt - other.totCnt;
        if (firstCmp != 0) {
            return firstCmp;
        }
        
        int secondCmp = other.singleOrBullCnt - this.singleOrBullCnt;
        if (secondCmp != 0) {
            return secondCmp;
        }
        
        return this.score - other.score;        
    }
    
    @Override
    public String toString() {
        return "Score : " + score + ", totCnt : " + totCnt + " singleOrBullCnt : " + singleOrBullCnt;
    }
}

class Solution {
    private List<Target> targets = new ArrayList<>();
    
    public int[] solution(int target) {
        setUp();
        
        int totCnt = 0;
        int singleOrBullCnt = 0;
        
        while (target >= 600) {
            if (target >= 300) {
                target -= 300;
                totCnt += 5;
                continue;
            }
        }
        
        int tempTotCnt = Integer.MAX_VALUE;
        int tempSingleOrBullCnt = -1;
        
        int[][] visited = new int[target+1][2];
        for (int idx=0; idx<visited.length; idx++) {
            visited[idx][0] = Integer.MAX_VALUE;
            visited[idx][1] = -1;
        }
        
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(target, 0, 0));
        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            
            if (cur.score == 0) {
                if (tempTotCnt > cur.totCnt) {
                    tempTotCnt = cur.totCnt;
                    tempSingleOrBullCnt = cur.singleOrBullCnt;
                } else if (tempTotCnt == cur.totCnt && tempSingleOrBullCnt < cur.singleOrBullCnt) {
                    tempTotCnt = cur.totCnt;
                    tempSingleOrBullCnt = cur.singleOrBullCnt;
                }
            
                continue;
            }
            
            for (Target t : targets) {
                int newScore = cur.score - t.score;
                if (newScore < 0) {
                    continue;
                }
                
                int newTotCnt = cur.totCnt + 1;
                if (visited[newScore][0] <= newTotCnt) continue;
                
                int newSingleOrBullCnt = cur.singleOrBullCnt;
                if (t.isSingleOrBull) { newSingleOrBullCnt++; }
                if (visited[newScore][1] >= newSingleOrBullCnt) continue;

                visited[newScore][0] = newTotCnt;
                visited[newScore][1] = newSingleOrBullCnt;
                pq.offer(new Node(newScore, newTotCnt, newSingleOrBullCnt));
            }
        }
        
        return new int[] { totCnt + tempTotCnt, singleOrBullCnt + tempSingleOrBullCnt };
    }
    
    private void setUp() {
        Set<Integer> temp = new HashSet<>();

        for (int score=1; score<21; score++) {
            targets.add(new Target(score, true));
            temp.add(score);
        }
        
        for (int score=1; score<21; score++) {
            if (!temp.contains(score*2)) {
                targets.add(new Target(score*2, false));
                temp.add(score*2);
            }
            
            if (!temp.contains(score*3)) {
                targets.add(new Target(score*3, false));
                temp.add(score*3);
            }
        }

        targets.add(new Target(50, true));
        targets.sort((a, b) -> b.score - a.score );
    }
}