/* References: https://github.com/Seanforfun/Algorithm-and-Leetcode/blob/master/leetcode/37.%20Sudoku%20Solver.md
    I could not find the exact same article that I referenced, but I know it had a similar solution to the one from this resource.
    The article and its code helped me work out the smaller details about implementing a sudoku solver.
    I knew I had to look through each row and column of the sudoku board, and find numbers to every empty space.
    However, I needed more guidance to figure out a way to implement the logic of testing potential answers.
    By using my reference I was able to better understand how to check if a solution was viable.
    For instance, I gained a better idea of how to check the specific grid a number was placed into.
*/

public class SudokuSolver {

    // method that calls function to solve sudoku board
    public static void solveSudoku(String[][] board) {
        // solves sudoku board in place
        solve(board);
        // displays solution to sudoku board
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                System.out.print(board[row][col] + " ");
            }
            System.out.println();
        }
    }

    // returns boolean value to indicate if sudoku board was solved
    public static boolean solve(String[][] board) {
        // traverse each row and col to test possible solutions
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                // solves for value in each empty square
                if (board[row][col] == ".") {
                    // checks if empty square was filled correctly
                    if(!fillSquare(board, row, col)) {
                        // sudoku board was not solved for current empty square
                        return false;
                    }                    
                }
            }
        }
        // sudoku board was solved for the current empty square
        return true;
    }

    // returns boolean value showing if square can be filled
    public static boolean fillSquare(String[][] board, int row, int col){
        // checks if potential number satisfies sudoku criteria
        for (int num = 1; num <= 9; num++) {
            // verifies potential number's validity
            if (validNum(board, row, col, num)){
                // if number is valid it is set in the previously empty square
                board[row][col] = Integer.toString(num);
                // checks again if potential number is viable solution
                // if not, empty square is put back as empty to test another number
                if (solve(board)) {
                    return true;
                }
                else {
                    board[row][col] = ".";
                }
            }
        }
        // square couldn't be filled
        return false;
    }

    // returns boolean value signifiying if potential number satisfies sudoku criteria
    public static boolean validNum(String[][] board, int row, int col, int num) {
        // checks potential sudoku board solution via rows, cols, and boxes
        for (int i = 0; i < 9; i++) {
            // sets box row to be checked
            int boxRow = row / 3;
            int localRow = i / 3;
            // sets box col to be checked
            int boxCol = col / 3;
            int localCol = i % 3;
            // checks if potential number can be placed in specific square
            if (board[row][i].equals(Integer.toString(num)) ||
                board[i][col].equals(Integer.toString(num)) || 
                board[boxRow * 3 + localRow][boxCol * 3 + localCol].equals(Integer.toString(num))) {
                return false;
            }
        }
        return true;
    }
    
    // main method initializes sudoku board and executes solve method
    public static void main(String[] args) {
        String[][] board = {{"5","3",".",".","7",".",".",".","."},
                {"6",".",".","1","9","5",".",".","."},
                {".","9","8",".",".",".",".","6","."},
                {"8",".",".",".","6",".",".",".","3"},
                {"4",".",".","8",".","3",".",".","1"},
                {"7",".",".",".","2",".",".",".","6"},
                {".","6",".",".",".",".","2","8","."},
                {".",".",".","4","1","9",".",".","5"},
                {".",".",".",".","8",".",".","7","9"}};
        solveSudoku(board);
    }
}