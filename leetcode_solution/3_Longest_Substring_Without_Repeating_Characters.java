import java.util.Arrays;
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int length = s.length();
        if(length == 0){
            return 0;
        }else if(length == 1){
            return 1;
        }else{

            int[] record = new int[length];
            Arrays.fill(record, 1);
            int i = 0;
            int j = 0;
            while(i <= length){
                while(i <= length - 1 && !(s.substring(j,i).contains(Character.toString(s.charAt(i))))){
                    i ++;
                }
                record[j] = i - j;
                if(i == length){
                    break;
                }else{
                    j = i - 1;
                    while(!s.charAt(i).equals(s.charAt(j))){
                        j --;
                    }
                    j++;
                }
            }
            int max = Arrays.stream(record).max().getAsInt();
            return max;

        }


    }
}