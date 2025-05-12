// Importing the Scanner to take the input from the keyboard
import java.util.Scanner;
// We write inside the public class because java is totally class based ,so public class ensurres the availibility of method to the Java Virtual machine
public class NotebookFactory {

    // Here it is main method  which is called by JVM
    public static void main(String[] args) {
        // Creating a object to take input from the keyboard
        Scanner sc = new Scanner(System.in);
// Letting the user know what to do ,so displaying statement

        System.out.println("How many times you want to test ");
        // Taking number of test cases
        int T = sc.nextInt();  // Number of test cases
// Running program for certain number of cases
        for (int i = 0; i < T; i++) {
            // Taking input of the pulp
            System.out.println("Enter the kgs of pulp you have ");
            
            int N = sc.nextInt();  
            int notebooks = N * 10;  
            System.out.println("The Number of books can be generated is :");
            System.out.println(notebooks);
        }
// Closing the scanner class object
        sc.close();
    }
}
