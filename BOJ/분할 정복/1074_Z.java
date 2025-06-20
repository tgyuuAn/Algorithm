import java.util.*;
import java.io.*;

class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    
    private static int targetR;
    private static int targetC;
    private static int nowStep = 0;
    
    private static void tokenizing() throws Exception {
        st = new StringTokenizer(br.readLine());
    }
    
    private static int nextInt() {
        return Integer.parseInt(st.nextToken());
    }
    
    public static void main(String[] args) throws Exception {
        tokenizing();
        int N = nextInt();
        targetR = nextInt();
        targetC = nextInt();
        
        divideAndConquer(0, (int)Math.pow(2,N), 0, (int)Math.pow(2,N));
    }
    
    public static void divideAndConquer(int startR, int endR, int startC, int endC) {
        
        if (endR - startR == 1) {
            nowStep++;

            if (startR == targetR && startC == targetC) {
                System.out.println(nowStep-1);
            }
            return;
        }
        
        int gap = endR-startR;
        if (startR <= targetR && targetR < startR+gap/2 && startC <= targetC && targetC < startC+gap/2) {
            divideAndConquer(startR, startR+gap/2, startC, startC+gap/2);
        } else if (startR <= targetR && targetR < startR+gap/2 && startC+gap/2 <= targetC && targetC < endC) {
            nowStep += gap/2*gap/2;
            divideAndConquer(startR, startR+gap/2, startC+gap/2, endC);
        } else if (startR+gap/2 <= targetR && targetR < endR && startC <= targetC && targetC < startC+gap/2){
            nowStep += gap/2*gap/2*2;
            divideAndConquer(startR+gap/2, endR, startC, startC+gap/2);
        } else {
            nowStep += gap/2*gap/2*3;
            divideAndConquer(startR+gap/2, endR, startC+gap/2, endC);
        }
        
        return;
    }
}