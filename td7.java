class td7 {
	static void loop1(int n) {
		  /*@ decreases n;
		   @*/
		  while (n > 0) n--;
		}

	static void loop2(int n) {
		  /*@ decreases 100 - n;
		   @*/
		  while (n < 100) n++;
		}
  
  public static void main(String[] args) {
	  
  }
}