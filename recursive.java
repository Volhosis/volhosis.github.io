import java.util.*;

public class recursive {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Type an integer and press enter.");
        int num = input.nextInt();

        input.close();

        System.out.println(exp(num, num));

    }
    
    public static int exp(int num, int pow) {
        
        System.out.println("Test");
        if(pow == 0) {

            return 1;

        } else {

            return num * exp(num, pow - 1);

        }
    }
}
