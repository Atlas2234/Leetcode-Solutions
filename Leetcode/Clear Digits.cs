public class Solution {
    public string ClearDigits(string s) {
        bool sentinel = false;
        int index = 0;
        int nonDigitIndex = -1;
        while (sentinel == false) {

            if (Char.IsNumber(s[index]) && nonDigitIndex != -1) {
                
                s = s.Remove(index,1);
                s = s.Remove(nonDigitIndex,1);
                index = 0;
                nonDigitIndex = -1;
            } else if (Char.IsNumber(s[index])) {
                index++;
            } else {
                index++;
                nonDigitIndex++;
            }

            if (index >= s.Length || s == "") {
                sentinel = true;
            }
        }

        return s;
    }
}