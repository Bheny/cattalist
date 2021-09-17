class Quadratic{
	public static void main(string []args){
		int a=2;
		int b=3;
		int c=4;

		double result;

		result = Math.sqrt((Math.pow(b,2)-4*(a*c)));
		result = -b+result;
		result = result/(2*a);

		System.out.println("X = " + result);

		result = Math.sqrt((Math.pow(b,2)-4*(a*c)));
		result = -b-result;
		result = result/(2*a);

	}
}