public class td7Dicho {
	/*@ requires t!= null && t.length > 0;
	  */
	static int binary_search(int t[], int v) {
        int l = 0, u = t.length - 1;
        /*
        @ loop_invariant 
        @		(l <= u+1 && 0 <= l && l <= t.length && -1 <= u && u < t.length )) ;
        @*/
        while (l <= u) {
            int m = (l + u) / 2;
            if (t[m] < v) l = m + 1;
            else if (t[m] > v) u = m - 1;
            else return m;
        }
        return - 1;
    }
}
