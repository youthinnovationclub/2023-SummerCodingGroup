import java.util.Random;
import java.util.Scanner;

public class FireworksPopGame {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Random random = new Random();

        System.out.println("Welcome to Fireworks Pop!");
        System.out.println("Try to guess the number of fireworks that will pop.");
        boolean PG=true;
        while(PG) {
            int RF = random.nextInt(10) + 1;


            System.out.print("Enter your guess (between 1 and 10): ");
            int UG = scan.nextInt();

            if (UG == RF) {
                System.out.println("Congratulations! You guessed correctly.");
            } else {
                System.out.println("Oops! That's incorrect. The number of fireworks was: " + RF);
            }
            System.out.println("Do you want to play guess the number of fireworks that will pop again?(0 for yes ,1 for no");
            int TPG = scan.nextInt();
            if(TPG==0){
                PG=true;
            }
            else{
                System.out.println("Thanks for participating in this game.");
                System.out.println("Hav a good day!!!");
                break;

            }
        }

    }
}
