public class Solution {
    /** 
     *@param A: A list of integers
     *@param elem: An integer
     *@return: The new length after remove
     */
    public int removeElement(int[] A, int elem) {
        // write your code here
        int j = 0;
        for (int i=0; i < A.length; i++) {
            if (A[i] != elem) {
                A[j] = A[i];
                j++;
            }
        }
        return j;
    }
	public static void main(String[] args) {
		int[] list = {1,1,2,3,4,1,5,6};
		int len = new Solution().removeElement(list, 1);
		//System.out.println(len);
		for (int i=0; i < len; i++) {
			System.out.printf("%d ",list[i]);
		}
		System.out.println();
	}
}
