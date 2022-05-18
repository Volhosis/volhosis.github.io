import java.util.*;

public class passwords {
    public static void main(String[] args) {

    int pass_length = 8;
    Random ran = new Random();
    String[] digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};
    String[] all_chars = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
    "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","*", "&", "$", "#"};
    
    double total_combinations = digits.length * Math.pow(all_chars.length, pass_length - 1);

    System.out.printf("There are %.0f different possible passwords that satisfy the constraint.\n", total_combinations);

    String random_pass = digits[ran.nextInt(digits.length)] + all_chars[ran.nextInt(all_chars.length)] + 
    all_chars[ran.nextInt(all_chars.length)] + all_chars[ran.nextInt(all_chars.length)] + 
    all_chars[ran.nextInt(all_chars.length)] + all_chars[ran.nextInt(all_chars.length)] + 
    all_chars[ran.nextInt(all_chars.length)] + all_chars[ran.nextInt(all_chars.length)];

    System.out.println("The random password is: " + random_pass);

    }

}