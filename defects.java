import java.util.*;

public class defects {
    public static void main(String[] args) {

        System.out.println("There is a probability of " + Double.toString(prob(100, 0)) + " to have no defects in a batch of 100 circuit boards. There is a probability of " + Double.toString(prob(100, 1)) + " to have 1 defect in a batch of 100 circuit boards. There is a probability of " + Double.toString(prob(100, 2)) + " to have 2 defects in a batch of 100 circuit boards. There is a probability of " + Double.toString(at_least(100, 3)) + " to have 3 or more defects in a batch of 100 circuit boards.");
    }

    public static double prob(int n, int defects) {
        double defect_prob = 0.01;

        return choose(n, defects) * Math.pow(defect_prob, defects) * Math.pow(1 - defect_prob, n - defects);
    }

    public static int choose(int n, int defects) {
        int num = 1;
        for(int i = n; i > n - defects; i--) {
            num *= i;
            num /= (n - i + 1);
        }
        return num;
    }

    public static double at_least(int n, int defects) {
        double total_prob = 0;
        for(int i = defects; i < n + 1; i++) {
            total_prob += prob(n, i);
        }

        return total_prob;
    }
}