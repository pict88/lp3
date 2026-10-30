#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int w[] = {2, 3, 4, 5};
    int v[] = {3, 4, 5, 6};
    int dp[5][6] = {};
    int W = 5;

    for (int i = 1; i <= 4; i++) {
        for (int j = 1; j <= W; j++) {
            if (w[i-1] <= j)
                dp[i][j] = max(v[i-1] + dp[i-1][j-w[i-1]], dp[i-1][j]);
            else
                dp[i][j] = dp[i-1][j];
        }
    }

    cout << "Maximum value = " << dp[4][W];
    return 0;
}
