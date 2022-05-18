public class graph {
    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 2, 1},
            {2, 1, 2, 1},
            {2, 2, 1, 2},
            {1, 1, 1, 0}
        };

        String[] labels = {"A ", "B ", "C ", "D "};

        System.out.println("  A B C D");
        
        for(int i = 0; i < matrix.length; i++) {
            System.out.print(labels[i]);
            for(int j = 0; j < matrix[0].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println("\nWalk: A-D-A-B\nTrail: A-D-B-A-C\nPath: A-B-C-D\nClosed walk: A-D-A-B-A\nCircuit: A-B-C-D-A\nCycle: A-B-C-D-A");


    }
}