import java.util.ArrayList;
import java.util.List;

class Solution {
    public String[] solution(String[] s) {
        List<String> answer = new ArrayList<String>();
        for (String input : s) {
            String replaced = replaceString(input);
            answer.add(replaced);
        }
        return answer.toArray(new String[0]);
    }
    
    public String replaceString(String input) {
        int useCount = 0;
        StringBuilder sb = new StringBuilder();
        
        for (int charIdx=0; charIdx<input.length(); charIdx++){
            char ch = input.charAt(charIdx);
            sb.append(ch);
            
            int sbLength = sb.length();
            if (sbLength >=3 &&
                sb.charAt(sbLength-3) == '1' &&
                sb.charAt(sbLength-2) == '1' &&
                sb.charAt(sbLength-1) == '0') {
                sb.delete(sbLength-3, sbLength);
                useCount++;
            }
        }
        
        int insertPos = sb.lastIndexOf("0");
        while (useCount-- > 0) {
            sb.insert(insertPos+1, "110");
        }
        
        return sb.toString();
    }
}