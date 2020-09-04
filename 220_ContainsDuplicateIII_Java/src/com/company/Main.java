import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] numList = {-1,2147483647};
        int k = 1;
        int t = 2147483647;
        System.out.println(solution.containsNearbyAlmostDuplicate(numList,k,t));
    }
}

class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
//        check null value
        if( k < 0 || t < 0) return false;
        Map<Integer, Integer> resultMap = new HashMap<Integer, Integer>();

//        start for loop
        int n = nums.length;
        for(int i = 0; i < n; i++){
            int level = (int) (nums[i]/((long)t + 1));
            if(nums[i] < 0){ level--; }

            System.out.println(level);
//            find the solution in the same level
            if( resultMap.containsKey(level) && ((i-resultMap.get(level)) <= k)) {return true;}
            else{
                resultMap.put(level,i);
                if(resultMap.containsKey(level - 1) && i - resultMap.get(level - 1) > k) {resultMap.remove(level-1);}
                if(resultMap.containsKey(level - 1) && ((long)nums[i] - (long)nums[resultMap.get(level - 1)]) <= t){return true;}
                if(resultMap.containsKey(level + 1) && i - resultMap.get(level + 1) > k) {resultMap.remove(level+1);}
                if(resultMap.containsKey(level + 1) && ((long)nums[resultMap.get(level + 1)] - (long)nums[i]) <= t){return true;}
            }
        }
        return false;
    }
}