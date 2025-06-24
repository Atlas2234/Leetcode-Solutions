public class Solution {
    public IList<int> FindKDistantIndices(int[] nums, int key, int k) {
        List<int> answer = new List<int>();
        var length = nums.Length;

        for (int i = 0; i < length; i++) {
            for (int j = 0; j < length; j++) {
                if (Math.Abs(i - j) <= k && nums[j] == key) {
                    answer.Add(i);
                    break;
                }
            }
        }

        return answer;
    }
}