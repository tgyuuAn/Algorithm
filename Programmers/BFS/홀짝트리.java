import java.util.*;

class Solution {
    HashMap<Integer, Set<Integer>> linked = new HashMap<>();
    
    public int[] solution(int[] nodes, int[][] edges) {        
        for (int node : nodes) {
            linked.put(node, new HashSet<>());
        }
        
        for (int[] edge : edges) {
            int a = edge[0];
            int b = edge[1];
            
            linked.get(a).add(b);
            linked.get(b).add(a);
        }

        HashMap<Integer, Boolean> visited = new HashMap<>();
        for (int node : nodes) {
            visited.put(node, false);
        }
        
        // 연결된 트리끼리 분리하기
        List<Set<Integer>> trees = new ArrayList<>();
        for (int node : nodes) {
            if (visited.get(node)) {
                continue;
            }
            
            Set<Integer> tree = new HashSet<>();
            ArrayDeque<Integer> deq = new ArrayDeque<>();
            deq.push(node);
            tree.add(node);
            visited.put(node, true);
            
            while(!deq.isEmpty()) {
                Integer cur = deq.pop();
                
                Set<Integer> neighbors = linked.get(cur);
                for (Integer neighbor : neighbors) {
                    if (visited.get(neighbor)) {
                        continue;
                    }
                    
                    deq.add(neighbor);
                    tree.add(neighbor);
                    visited.put(neighbor, true);
                }
            }
            
            trees.add(tree);
        }
        
        int[] answer = new int[2];        
        for (Set<Integer> tree : trees) {
            Set<Integer> reverse = new HashSet<Integer>();
            Set<Integer> normal = new HashSet<Integer>();
            
            for (Integer node : tree) {
                if (node%2==0 && linked.get(node).size()%2==0) {
                    normal.add(node);
                    continue;
                }
                
                if (node%2==1 && linked.get(node).size()%2==1) {
                    normal.add(node);
                    continue;
                }
                
                reverse.add(node);
            }
             
            if (isValidNormalTree(normal, reverse, tree)) {
                answer[0]++;
            }
            
            if (isValidReverseTree(normal, reverse, tree)) {
                answer[1]++;
            }
        }
    
        return answer;
    }
    
    private boolean isValidNormalTree(
        Set<Integer> normal,
        Set<Integer> reverse,
        Set<Integer> tree
    ) {
        if (normal.isEmpty()) {
            return false;
        }
                
        for (Integer node : normal) {
            ArrayDeque<Integer> deq = new ArrayDeque<>();
            Set<Integer> visited = new HashSet<>();
            deq.push(node);
            visited.add(node);
            
            while (!deq.isEmpty()) {
                Integer curNode = deq.pop();
                boolean isEven = curNode%2==0;
                int childCnt = 0;
                
                for (Integer neighbor : linked.get(curNode)) {
                    if (neighbor == node) {
                        continue;
                    }
                    
                    if (visited.contains(neighbor)) {
                        continue;
                    }
                    
                    deq.add(neighbor);
                    visited.add(neighbor);
                    childCnt++;
                }
                
                if (isEven != (childCnt%2==0)) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
    private boolean isValidReverseTree(
        Set<Integer> normal,
        Set<Integer> reverse,
        Set<Integer> tree
    ) {
        if (reverse.isEmpty()) {
            return false;
        }
        
        for (Integer node : reverse) {
            ArrayDeque<Integer> deq = new ArrayDeque<>();
            Set<Integer> visited = new HashSet<>();
            deq.push(node);
            visited.add(node);
            
            while (!deq.isEmpty()) {
                Integer curNode = deq.pop();
                boolean isEven = curNode%2==0;
                
                int childCnt = 0;
                for (Integer neighbor : linked.get(curNode)) {
                    if (neighbor == node) {
                        continue;
                    }
                    
                    if (visited.contains(neighbor)) {
                        continue;
                    }
                    
                    deq.add(neighbor);
                    visited.add(neighbor);
                    childCnt++;
                }
                
                if (isEven == (childCnt%2==0)) {
                    return false;
                }
            }
        }
        
        return true;
    }
}