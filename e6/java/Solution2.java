class Solution2 {
    /**
     * @param A and B: sorted integer array A and B.
     * @return: A new sorted integer array
     */
    public int[] mergeSortedArray(int[] A, int[] B) {
        // Write your code here
		int[] shortArray, longArray;
		shortArray = A.length < B.length ? A : B;
		longArray = A.length >= B.length ? A : B;
		
		int newbegin = 0;
		int[] result = new int[A.length+B.length];
		int resultIdx = 0;
		for (int i=0; i<shortArray.length; i++) {
			int tmp = shortArray[i];
			if (tmp <= longArray[newbegin]) {
				result[resultIdx] = tmp;
				resultIdx++;
			}
			else if (tmp >= longArray[longArray.length-1]) {
				/*
				System.out.println(" tmp > longArray.max");
				System.out.println(newbegin);
				System.out.println(resultIdx);
				System.out.println(A.length+B.length-resultIdx);
				*/
				System.arraycopy(longArray, newbegin, result, resultIdx, longArray.length - newbegin);
				System.arraycopy(shortArray, i, result, resultIdx+longArray.length-newbegin, shortArray.length - i);
				newbegin = longArray.length;
				resultIdx = A.length+B.length;
				break;
			}
			else {
				System.out.println(" tmp between longArray.min and longArray.max");
				int idx = find(longArray, tmp);
				/*
				System.out.println(newbegin);
				System.out.println(resultIdx);
				System.out.println(idx-newbegin);
				*/
				System.arraycopy(longArray, newbegin, result, resultIdx, idx-newbegin);
				resultIdx += idx-newbegin;
				newbegin = idx;
				result[resultIdx++] = tmp;
			}
		}
        if (newbegin < longArray.length)
			System.arraycopy(longArray, newbegin, result, resultIdx, longArray.length-newbegin);
		return result;
    }

	public static int find(int[] array, int e) {
		if (e <= array[0])
			return 0;
		if (e >= array[array.length-1])
			return array.length;
		int lp = 0;
		int rp = array.length - 1;
		while (rp -lp > 1) {
			int mid = (lp + rp) / 2;
			if (array[mid] > e) {
				rp = mid;
			}
			else {
				lp = mid;
			}
		}
		return rp;
	}

	public static void main(String[] args) {
		int[] a = {1,3,5};
		int[] b = {1,2,3,4,5};
		int[] newArray = new Solution2().mergeSortedArray(a, b);
		for (int i:newArray) {
			System.out.println(i);
		}
	}
}
