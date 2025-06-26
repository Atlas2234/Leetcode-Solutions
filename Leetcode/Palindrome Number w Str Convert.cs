public class Solution {
    public bool IsPalindrome(int x) {
        string s = x.ToString();
        
        int mid;
        string shalf1;
        string shalf2;

        if (s.Length == 1) {
            return true;
        }
        else if (s.Length % 2 != 0) {
            mid = s.Length / 2;
            shalf1 = s.Substring(0, mid);
            shalf2 = s.Substring(mid + 1);
            Console.WriteLine("1 " + shalf1 + " : " + shalf2);
        } else {
            mid = (s.Length / 2) - 1;
            shalf1 = s.Substring(0, mid + 1);
            shalf2 = s.Substring(mid + 1);
            Console.WriteLine("2 " + shalf1 + " : " + shalf2);
        }

        int j = shalf1.Length - 1;
        for (int i = 0; i < shalf1.Length; i++) {
            if (shalf1[i] != shalf2[j]) {
                return false;
            } else {
                j--;
            }
        }

        return true;
    }
}