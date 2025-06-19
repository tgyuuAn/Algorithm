import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;

    private static int maxScore = 0;
    private static int[] nextIdx;
    private static int[] shortcutIdx;
    private static int[] score;
    private static int[] dices;
    
    private static void tokenizing() throws Exception { 
        st = new StringTokenizer(br.readLine()); 
    }
    
    private static int nextInt() {
        return Integer.parseInt(st.nextToken());
    }
    
    private static void setUp() {
        nextIdx = new int[33];
        shortcutIdx = new int[33];
        score = new int[33];
        
        for (int idx=0; idx<32; idx++) {
            nextIdx[idx] = idx+1;
            shortcutIdx[idx] = idx+1;
            score[idx] = idx*2;
        }
        
        shortcutIdx[5] = 22;
        shortcutIdx[10] = 26;
        
        shortcutIdx[27] = 25;
        nextIdx[27] = 25;
        
        shortcutIdx[15] = 28;
        shortcutIdx[30] = 25;
        nextIdx[30] = 25;
        
        nextIdx[25] = 31;
        shortcutIdx[25] = 31;
        
        nextIdx[32] = 20;
        shortcutIdx[32] = 20;
        
        nextIdx[21] = 21;
        shortcutIdx[21] = 21;
              
        score[22] = 13;
        score[23] = 16;
        score[24] = 19;
        score[25] = 25;
    
        score[26] = 22;
        score[27] = 24;
        
        score[28] = 28;
        score[29] = 27;
        score[30] = 26;
        
        score[31] = 30;
        score[32] = 35;
        score[21] = 0;
    }
    
    public static void main(String[] args) throws Exception {
        tokenizing();
        int count = st.countTokens();
        int[] temp = new int[count];
        
        for (int i=0; i<count; i++) {
            temp[i] = nextInt();
        }
        
        dices = temp;
        setUp();
        backTracking(new int[4], 0, 0);
        System.out.println(maxScore);
    }
    
    private static void backTracking(int[] dicesCurIdxes, int step, int curScore) {
        if (curScore > maxScore) {
            maxScore = curScore;
        }
        
        if (step == dices.length) {
            return;
        }
            
        for (int idx=0; idx<dicesCurIdxes.length; idx++) {
            int curIdx = dicesCurIdxes[idx];
                
            if (curIdx == 21) {
                continue;
            }
                
            int origin = curIdx;
            int moveCount = dices[step];
            for (int cnt=0; cnt<moveCount; cnt++) {
                int now = dicesCurIdxes[idx];
                    
                if (cnt == 0) {
                    // 첫번째 시작 위치에서는 파란색 화살표 우선 이동
                    dicesCurIdxes[idx] = shortcutIdx[now];
                } else {
                    // 그 외에는 빨간 화살표 따라 이동
                    dicesCurIdxes[idx] = nextIdx[now];
                }
            }
            
            boolean isDuplication = false;
            for (int idxForCheck=0; idxForCheck<dicesCurIdxes.length; idxForCheck++) {
                if (idxForCheck == idx) {
                    continue;
                }
                
                if (dicesCurIdxes[idxForCheck] == dicesCurIdxes[idx] && dicesCurIdxes[idx] != 21) {
                    dicesCurIdxes[idx] = origin;
                    isDuplication = true;
                    break;
                }
            }
            
            if (isDuplication) {
                continue;
            }
                
            backTracking(dicesCurIdxes, step+1, curScore + score[dicesCurIdxes[idx]]);
            dicesCurIdxes[idx] = origin;
        }
        
        return;
    }
}