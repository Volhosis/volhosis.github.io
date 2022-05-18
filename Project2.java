import java.util.*;

public class Project2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        while(true) {
            System.out.println("Pick a function by typing its number:\n\n1. t: Z --> Z. t(x) = 3x\n2. t: Z --> Z. t(x) = x^2\n3. t: Z --> Z. t(x) = 2x - 2");
            int user_input = input.nextInt();
            System.out.println(determineInjective(user_input));
        }
    }

    public static String determineInjective(int in) {

        if(in == 1) {
            for(int i = 1; i < 101; i++) {
                for(int j = i + 1; j < 101; j++) {
                    if(3 * i == 3 * j) {
                        return "That function is not injective.";
                    }
                }
            }
            return "That function is injective.";
        }
        else if(in == 2) {
            for(int i = 1; i < 101; i++) {
                for(int j = i + 1; j < 101; j++) {
                    if(Math.pow(i, 2) == Math.pow(j, 2)) {
                        return "That function is not injective.";
                    }
                }
            }
            return "That function is injective.";
        }
        else if(in == 3) {
            for(int i = 1; i < 101; i++) {
                for(int j = i + 1; j < 101; j++) {
                    if(2 * i - 2 == 2 * j - 2) {
                        return "That function is not injective.";
                    }
                }
            }
            return "That function is injective.";
        }
        else{
            return "Your input was not recognized. Please try again.";
        }
    }
}