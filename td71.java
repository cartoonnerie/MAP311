import java.lang.Math;
public class td71 {
	
	//@ requires i >= 0;  
	//@ ensures \result == 0;
	  static int loop3(int i) {
		  /*@ loop_invariant
		   @	i >= 0;
		   @decreases i;
		   @*/
	      while (i > 0)
	        i--;
	      return i;
	  }
	  public static void main(String[] args) {
//		  for (int j = 0 ; j< 10 ; j++){
//			  loop3((int) (Math.random()*50));
//		  }
		  int x = 1;
		  if (x >= 0)
		  loop3(x);
	  
	}
}
