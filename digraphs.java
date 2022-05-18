public class digraphs {
    public static void main(String[] args) {
        int[][] matrix1 = {
            {5,4,0,1},
            {2,1,3,1},
            {0,8,1,0},
            {1,7,5,3}
        };
        int[][] matrix2 = {
            {0,1,5,1},
            {1,2,0,8},
            {3,4,9,1},
            {1,0,7,6}
        };

        if(matrix1[0].length == matrix2.length) {
            int[][] matrix3 = mult(matrix1, matrix2);
            System.out.println(print(matrix3));
        }else{
            System.out.println("Those two matrices cannot be multiplied.");
        }
    }

    public static int[][] mult(int[][] matrix1, int[][] matrix2) {
        int[][] out = new int[matrix1.length][matrix2[0].length];

        for(int i = 0; i < out.length; i++) {
            for(int j = 0; j < out[0].length; j++) {
                out[i][j] = 0;
                for(int k = 0; k < matrix2.length; k++) {
                    out[i][j] += matrix1[i][k] * matrix2[k][j];
                }
            }
        }

        return out;
    }

    public static String print(int[][] matrix) {
        String str = "";

        for(int i = 0; i < matrix.length; i++) {
            str += "[";
            for(int j = 0; j < matrix[0].length; j++) {
                str += matrix[i][j] + " ";
            }
            str = str.substring(0, str.length() - 1) + "]\n";
        }

        return str;
    }
}