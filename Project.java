import java.util.*;

public class Project {
    public static void main(String[] args) {
            Scanner input = new Scanner(System.in);

            System.out.println("Enter the first set of integers (from 1 to 100) Example: \"1,2,3,4\" without quotations:");
            String[] set1 = input.nextLine().replace(" ", "").split(",");
            System.out.println("Enter the second set of integers (from 1 to 100) Example: \"1,2,3,4\" without quotations:");
            String[] set2 = input.nextLine().replace(" ", "").split(",");

            System.out.println("\n\n\n" + "S = " + convert_set(set1) + '\n' + "T = " + convert_set(set2) + "\n\nP(S) = " 
            + power_set(set1) + "\nS x T = " + cartesian_product(set1, set2) + "\nS UNION T = " + union(set1, set2) + 
            "\nS INTERSECT T = " + intersection(set1, set2) + "\nS - T = " + difference(set1, set2) + "\nComplement(S) = " 
            + complement(set1) + "\n");

            input.close();
    }

    public static String convert_set(String[] set) {
        String out = "{";
        for(String str : set) {
            out += str + ',';
        }
        out = out.substring(0, out.length() - 1) + '}';

        return out;
    }

    public static String power_set(String[] set) {
        String out = "{{";
        int combinations = (int) Math.pow(2, set.length);

        for(int i = 0; i < combinations; i++) {
            String temp = "{";

            for(int j = 0; j < set.length; j++) {
                if((i & (int) Math.pow(2, j)) > 0) {
                    temp += set[j] + ',';
                }
            }

            temp = temp.substring(0, temp.length() - 1) + "},";
            out += temp;

        }

        out = out.substring(0, out.length() - 1) + "}";

        return out;
    }

    public static String cartesian_product(String[] set1, String[] set2) {
        String out = "{";

        for(int i = 0; i < set1.length; i++) {
            for(int j = 0; j < set2.length; j++) {
                out += "(" + set1[i] + "," + set2[j] + "),";
            }
        }

        out = out.substring(0, out.length() - 1) + "}";

        return out;
    }
    public static String union(String[] set1, String[] set2) {
        String out = convert_set(set1);
        out = out.substring(0, out.length() - 1) + ",";

        for(String str : set2) {
            if(!Arrays.stream(set1).anyMatch(str::equals)) {
                out += str + ",";
            }
        }

        out = out.substring(0, out.length() - 1) + "}";

        return out;
    }
    public static String intersection(String[] set1, String[] set2) {
        String out = "{";

        for(String str : set2) {
            if(Arrays.stream(set1).anyMatch(str::equals)) {
                out += str + ",";
            }
        }

        if(out.length() > 2) out = out.substring(0, out.length() - 1);
        out += "}";

        return out;
    }
    public static String difference(String[] set1, String[] set2) {
        String out = "{";

        for(String str : set1) {
            if(!Arrays.stream(set2).anyMatch(str::equals)) {
                out += str + ",";
            }
        }

        if(out.length() > 1) out = out.substring(0, out.length() - 1);
        out += "}";

        return out;
    }
    public static String complement(String[] set) {
        String[] U = new String[100];
        for(int i = 0; i < U.length; i++) {
            U[i] = Integer.toString(i + 1);
        }

        return difference(U, set);
    }
}