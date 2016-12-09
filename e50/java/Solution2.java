import java.util.ArrayList;

public class Solution2 {

	public static ArrayList<Long> productExcludeItSelf(ArrayList<Integer> A) {
		ArrayList<Long> ret =  new ArrayList<Long>(A.size());
		if (A.size() < 2) {
			ret.add(1L);
			return ret;
		}
		class QuotientRemainder {
			public int q;
			public int r;
			public QuotientRemainder(int q, int r) {
				this.q = q;
				this.r = r;
			}
		}

		ArrayList<QuotientRemainder> qrs = new ArrayList<QuotientRemainder>();
		ArrayList<ArrayList<Long>> productCache = new ArrayList<ArrayList<Long>>();
		int nMulti = A.size() - 1;
		while (nMulti > 1) {
			int q = nMulti / 2;
			int r = nMulti % 2;
			QuotientRemainder qr = new QuotientRemainder(q, r);
			qrs.add(qr);
			nMulti = q;
		}
		ArrayList<Long> init = new ArrayList<Long>(A.size());
		for (int i=0; i < A.size(); i++) {
			init.add(Long.valueOf(A.get(i)));
		}
		productCache.add(init);
		for (int i=qrs.size()-1; i >= 0; i--) {
			int q = qrs.get(i).q;
			int r = qrs.get(i).r;
			ArrayList<Long> cache = new ArrayList<Long>();
			if (r == 1) {
				for (int j=0; j < A.size(); j++) {
					Long temp = productCache.get(qrs.size()-i-1).get(j) * productCache.get(qrs.size()-i-1).get((j+q)%A.size()) * productCache.get(0).get((j+2*q)%A.size());
					cache.add(temp);
					//System.out.println(temp);
				}
			}
			else {
				for (int j=0; j < A.size(); j++) {
					Long temp = productCache.get(qrs.size()-i-1).get(j) * productCache.get(qrs.size()-i-1).get((j+q)%A.size());
					cache.add(temp);
					//System.out.println(temp);
				}
			}
			productCache.add(cache);
		}
		for (int i=0; i < A.size(); i++) {
			ret.add(productCache.get(productCache.size()-1).get((i+1)%A.size()));
		}
		return ret;
	}
	public static void main(String[] args) {
		int length = 21;
		if (args.length > 0) {
			length = Integer.valueOf(args[0]);
		}
		ArrayList<Integer> input =  new ArrayList<Integer>(Integer.valueOf(length));
		for (int i=0; i < length; i++) {
			input.add(1);
		}
		ArrayList<Long> product = productExcludeItSelf(input);
		for (int i=0; i < length; i++) {
			System.out.print(product.get(i).toString() + ' ');
		}
	}
}
