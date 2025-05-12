import java.util.Scanner;

public class maxtriangleperi{
    public static void main(String[] args) {
        // Creating object
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the nuber of test cases");
        int T = sc.nextInt();
        // Looping fot all test cases
        while (T-- > 0) {
            System.out.println("Enter the N sides");
            int N = sc.nextInt();
            if (N <= 3) {
                // As for 3 or less triangle rules not follow
                System.out.println(-1);
            } else {
                // Max Perimeter N+N-1+N-2
                System.out.println(3 * N - 3);
            }
        }
        // Closing Scanner class object
        sc.close();
    }
}