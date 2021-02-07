
public class Problem2 {

	public static long fib(long number) {
		if (number == 1 || number == 2)
			return number;
		else
			return fib(number-1) + fib (number-2);
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		long sum = 0;
		long index = 0;
		long fibret = 0;
		
		while (fibret < 4000000)
		{
			 fibret = fib(++index);
			if (fibret % 2 == 0) sum += fibret;
		}
		System.out.println("Final sum was " + sum);

	}

}
