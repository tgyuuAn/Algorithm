import java.util.*;

class Trie {
    private TrieNode root = new TrieNode(' ');
    
    public void addWord(String word) {
        TrieNode node = root;

        for (int charIdx=0; charIdx<word.length(); charIdx++) {
            char cur = word.charAt(charIdx);
            
            if (node.children.containsKey(cur)) {
                node = node.children.get(cur);
                node.size++;
            } else {
                node.addChildren(cur);
                node = node.children.get(cur);
            }
        }
    }
    
    public int findWord(String word) {
        int count=0;
        TrieNode node = root;
        
        for (int charIdx=0; charIdx<word.length(); charIdx++) {
            Character cur = word.charAt(charIdx);
            
            node = node.children.get(cur);
            count++;
            
            if (node.size == 0) {
                return count;
            }            
        }
        
        return count;
    }
}

class TrieNode {
    public int size=0;
    public HashMap<Character, TrieNode> children = new HashMap();
    
    private Character cur;
    
    public TrieNode(Character cur) {
        this.cur = cur;
    }
    
    public void addChildren(Character cur) {
        children.put(cur, new TrieNode(cur));
    }
}

class Solution {
    public int solution(String[] words) {
        Trie trie = new Trie();
        
        for (String word : words) {
            trie.addWord(word);
        }

        int answer = 0;
        for (String word : words) {
            answer += trie.findWord(word);
        }
        
        return answer;
    }
}