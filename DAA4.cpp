#include <iostream>
using namespace std;

int N;
int board[20][20] = {0};

bool isSafe(int row, int col) {

    for(int i = 0; i < col; i++)
        if(board[row][i])
            return false;

    for(int i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if(board[i][j])
            return false;

    for(int i = row, j = col; i < N && j >= 0; i++, j--)
        if(board[i][j])
            return false;

    return true;
}

bool solve(int col) {

    if(col == N)
        return true;

    for(int row = 0; row < N; row++) {

        if(isSafe(row, col)) {

            board[row][col] = 1;

            if(solve(col + 1))
                return true;

            board[row][col] = 0;
        }
    }

    return false;
}

int main() {

    cout << "Enter N: ";
    cin >> N;

    board[0][0] = 1;

    if(solve(1)) {

        cout << "\nSolution:\n";

        for(int row = 0; row < N; row++) {
            for(int col = 0; col < N; col++)
                cout << board[row][col] << " ";
            cout << endl;
        }
    }
    else {
        cout << "No Solution";
    }

    return 0;
}
