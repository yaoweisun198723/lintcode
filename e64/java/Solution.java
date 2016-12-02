class Solution {
    /**
     * @param A: sorted integer array A which has m elements, 
     *           but size of A is m+n
     * @param B: sorted integer array B which has n elements
     * @return: void
     */
    public void mergeSortedArray(int[] A, int m, int[] B, int n) {
        // write your code here
        int idxA = m - 1;
        int idxB = n - 1;
        for (int i=m+n-1; i >= 0; i--) {
            if (idxA < 0) {
                A[i] = B[idxB];
                idxB--;
            }
            else if (idxB < 0) {
                A[i] = A[idxA];
                idxA--;
            }
            else if (A[idxA] < B[idxB]) {
                A[i] = B[idxB];
                idxB--;
            }
            else {
                A[i] = A[idxA];
                idxA--;
            }
        }
    }
}
