public class td7Q3 {
/*@ requires t != null;
  @ ensures \result <==> (\forall int i; 0 <= i && i < t.length; t[i]==0);
  @*/
static boolean all_zeros(int t[]) {
    /*@ decreases   t.length - k;
     @ loop_invariant 
     @		(\forall int i; 0 <= i && i < k ==> t[i]==0) &&
     @		k >= 0 && k <= t.length;
     @*/
    for (int k = 0; k < t.length; k++) {
      if (t[k] != 0)
        return false;
    }
    return true;
}
}
