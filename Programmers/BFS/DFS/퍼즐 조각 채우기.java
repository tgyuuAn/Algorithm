import java.util.*;
import java.util.stream.Collectors;

class Solution {
    private int rowLength;
    private int colLength;
    private int[] dx = {0, 0, -1, 1};
    private int[] dy = {-1, 1, 0, 0};

    public int solution(int[][] game_board, int[][] table) {
        rowLength = game_board.length;
        colLength = game_board[0].length;

        List<List<Integer[]>> pieces = classify(table, 1);
        List<List<Integer[]>> holes = classify(game_board, 0);
        boolean[] visited = new boolean[pieces.size()];
        int answer = 0;

        for (List<Integer[]> hole : holes) {
            for (int i = 0; i < pieces.size(); i++) {
                if (visited[i]) continue;

                List<Integer[]> piece = pieces.get(i);
                if (hole.size() != piece.size()) continue;

                boolean matched = false;
                for (int rot = 0; rot < 4; rot++) {
                    piece = rotatePiece(piece);
                    List<Integer[]> sortedHole = new ArrayList<>(hole);
                    List<Integer[]> sortedPiece = new ArrayList<>(piece);

                    sortedHole.sort(Comparator.comparingInt((Integer[] a) -> a[0])
                                              .thenComparingInt(a -> a[1]));
                    sortedPiece.sort(Comparator.comparingInt((Integer[] a) -> a[0])
                                               .thenComparingInt(a -> a[1]));

                    boolean isSame = true;
                    for (int j = 0; j < hole.size(); j++) {
                        Integer[] h = sortedHole.get(j);
                        Integer[] b = sortedPiece.get(j);
                        if (h[0] != b[0] || h[1] != b[1]) {
                            isSame = false;
                            break;
                        }
                    }

                    if (isSame) {
                        visited[i] = true;
                        answer += piece.size();
                        matched = true;
                        break;
                    }
                }

                if (matched) break;
            }
        }

        return answer;
    }

    private List<List<Integer[]>> classify(int[][] board, int target) {
        List<List<Integer[]>> blocks = new ArrayList<>();
        boolean[][] visited = new boolean[rowLength][colLength];

        for (int r = 0; r < rowLength; r++) {
            for (int c = 0; c < colLength; c++) {
                if (visited[r][c] || board[r][c] != target) continue;

                List<Integer[]> block = new ArrayList<>();
                Queue<Integer[]> queue = new LinkedList<>();
                queue.add(new Integer[]{r, c});
                visited[r][c] = true;

                while (!queue.isEmpty()) {
                    Integer[] cur = queue.poll();
                    block.add(cur);

                    for (int dir = 0; dir < 4; dir++) {
                        int nr = cur[0] + dy[dir];
                        int nc = cur[1] + dx[dir];

                        if (nr < 0 || nr >= rowLength || nc < 0 || nc >= colLength) continue;
                        if (!visited[nr][nc] && board[nr][nc] == target) {
                            visited[nr][nc] = true;
                            queue.add(new Integer[]{nr, nc});
                        }
                    }
                }

                int minR = Integer.MAX_VALUE;
                int minC = Integer.MAX_VALUE;
                for (Integer[] b : block) {
                    minR = Math.min(minR, b[0]);
                    minC = Math.min(minC, b[1]);
                }

                int finalMinR = minR;
                int finalMinC = minC;
                List<Integer[]> normalized = block.stream()
                        .map(b -> new Integer[]{b[0] - finalMinR, b[1] - finalMinC})
                        .collect(Collectors.toList());

                blocks.add(normalized);
            }
        }

        return blocks;
    }

    private List<Integer[]> rotatePiece(List<Integer[]> piece) {
        List<Integer[]> rotated = new ArrayList<>();
        for (Integer[] p : piece) {
            rotated.add(new Integer[]{p[1], -p[0]});
        }

        int minR = Integer.MAX_VALUE;
        int minC = Integer.MAX_VALUE;
        for (Integer[] b : rotated) {
            minR = Math.min(minR, b[0]);
            minC = Math.min(minC, b[1]);
        }

        int finalMinR = minR;
        int finalMinC = minC;

        return rotated.stream()
                .map(b -> new Integer[]{b[0] - finalMinR, b[1] - finalMinC})
                .collect(Collectors.toList());
    }
}
