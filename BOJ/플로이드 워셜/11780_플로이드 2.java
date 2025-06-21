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
        int M = nextInt();
        
        int[][] cost = new int[N+1][N+1];
        for (int i=0; i<N+1; i++) {
            Arrays.fill(cost[i], Integer.MAX_VALUE);
            cost[i][i] = 0;
        }
        
        List<Integer>[][] path = new ArrayList[N+1][N+1];
        for (int i=0; i<N+1; i++) {
            for (int j=0; j<N+1; j++) {
                path[i][j] = new ArrayList<>();
            }

            path[i][i].add(i);
        }
        
        for (int i=0; i<M; i++) {
            tokenizing();
            int a = nextInt();
            int b = nextInt();
            int c = nextInt();
            cost[a][b] = Math.min(cost[a][b], c);
        }
        
        for (int mid=1; mid<N+1; mid++) {
            for (int start=1; start<N+1; start++) {
                for (int end=1; end<N+1; end++) {
                    if (start == mid || start == end || mid == end) {
                        continue;
                    }
                    
                    if (cost[start][mid] != Integer.MAX_VALUE && cost[mid][end] != Integer.MAX_VALUE) {
                        if (cost[start][end] > cost[start][mid] + cost[mid][end]) {
                            cost[start][end] = cost[start][mid] + cost[mid][end];

                            List<Integer> joined = new ArrayList<>();
                            joined.addAll(path[start][mid]);
                            joined.add(mid);
                            joined.addAll(path[mid][end]);
                            path[start][end] = joined;
                        }
                    }
                }
            }
        }
        
        for (int i=1; i<N+1; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j=1; j<N+1; j++) {
                sb.append(cost[i][j] == Integer.MAX_VALUE ? 0 : cost[i][j]);
                sb.append(" ");
            }
            System.out.println(sb.toString().trim());
        }
        
        for (int i=1; i<N+1; i++) {
            for (int j=1; j<N+1; j++) {
                if (i==j) {
                    System.out.println("0");
                    continue;
                }
                
                if (cost[i][j] == Integer.MAX_VALUE) {
                    System.out.println("0");
                    continue;
                }

                if (path[i][j].isEmpty()) {
                    System.out.printf("2 %d %d\n", i, j);
                    continue;
                }
                
                StringBuilder sb = new StringBuilder();
                sb.append(path[i][j].size()+2);
                sb.append(" " + i +" ");
                for (Integer history : path[i][j]) {
                    sb.append(history);
                    sb.append(" ");
                }
                sb.append(j);
                System.out.println(sb.toString());
            }
        }
    }
}