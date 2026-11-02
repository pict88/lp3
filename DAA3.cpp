#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int w[] = {2, 3, 4, 5};
    int v[] = {3, 4, 5, 6};
    int W = 5;
    int dp[5][6] = {0};

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j <= W; j++) {
            // Choice 1: Leave item i
            dp[i + 1][j] = dp[i][j];

            // Choice 2: Take item i (if it fits)
            if (j >= w[i]) {
                dp[i + 1][j] = max(dp[i + 1][j], v[i] + dp[i][j - w[i]]);
            }
        }
    }

    cout << "Maximum value = " << dp[4][W];
    return 0;
}
