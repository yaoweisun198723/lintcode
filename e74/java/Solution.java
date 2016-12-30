/**
 * public class SVNRepo {
 *     public static boolean isBadVersion(int k);
 * }
 * you can use SVNRepo.isBadVersion(k) to judge whether 
 * the kth code version is bad or not.
*/
class Solution {
    /**
     * @param n: An integers.
     * @return: An integer which is the first bad version.
     */
    public int findFirstBadVersion(int n) {
        // write your code here
        if (SVNRepo.isBadVersion(1)) {
            return 1;
        }
        if (!SVNRepo.isBadVersion(n)) {
            return -1;
        }
        int left = 1;
        int right = n;
        while (right - left > 1) {
            int mid = (left + right) / 2;
            if (SVNRepo.isBadVersion(mid)) {
                right = mid;
            }
            else {
                left = mid;
            }
        }
        return right;

    }
}
