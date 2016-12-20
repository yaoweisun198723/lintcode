class Solution1 {
    /**
     * @param A and B: sorted integer array A and B.
     * @return: A new sorted integer array
     */
    public int[] mergeSortedArray(int[] A, int[] B) {
        // Write your code here
		int sza = A.length;
		int szb = B.length;
		int pa = 0;
		int pb = 0;
		int[] ret = new int[sza+szb];
		for (int i=0; i < sza+szb; i++) {
			if (pa >= sza) {
				ret[i] = B[pb];
				pb++;
			}
			else if (pb >= szb) {
				ret[i] = A[pa];
				pa++;
			}
			else {
				if (A[pa] < B[pb]) {
					ret[i] = A[pa];
					pa++;
				}
				else {
					ret[i] = B[pb];
					pb++;
				}
			}
		}
		return ret;
    }

	public static void main(String[] args) {
		int[] a = {1,3,5};
		int[] b = {1,2,3,4,5};
		int[] newArray = new Solution1().mergeSortedArray(a, b);
		for (int i:newArray) {
			System.out.println(i);
		}
	}
}
