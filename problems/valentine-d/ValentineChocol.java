// Importing Scanner to take input from the user via keyboard
import java.util.Scanner;

// This is the main class where the program runs.
// Java needs everything inside a class, and public class ensures JVM can access it directly.
public class ValentineChocol {

    // This is the main method — the entry point of every Java program. JVM starts execution from here.
    public static void main(String[] args) {

        // Creating a Scanner object to accept user input from the console
        Scanner sc = new Scanner(System.in);

        // Asking the user how many times they want to test (number of test cases)
        System.out.println("How many test cases do you want to run?");

        int T = sc.nextInt(); // Reading the number of test cases

        // Running the program logic for each test case
        for (int i = 0; i < T; i++) {

            // Asking the user to enter the total money and cost of one chocolate
            System.out.println("Enter the money Ayushman has and enter the cost of one choclate (use space):");

            int X = sc.nextInt(); // Money Ayushman has
            System.out.println("");
            int Y = sc.nextInt(); // Cost of one chocolate
            if(Y==0)
            {
                System.out.println("He can buy any number of choclate");
                continue;
            }


            // Calculating how many chocolates Ayushman can buy using integer division
            int maxChocolates = X / Y;

            // Displaying the result
            System.out.println("Maximum number of chocolates Ayushman can buy:");
            System.out.println(maxChocolates);
        }

        // Closing the Scanner to free system resources
        sc.close();
    }
}
