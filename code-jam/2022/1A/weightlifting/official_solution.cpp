#include <iostream>
#include <string.h>

using namespace std;

int MAX = 2e6;

int main(int argc, char *argv[]) {
    int t;
    cin >> t;
    for (int it = 1; it <= t; it++) {
        int e, w;
        cin >> e >> w;
        int x[e][w];
        for (int i = 0; i < e; i++)
            for (int j = 0; j < w; j++)
                cin >> x[i][j];

        // Compute common sets of weights
        int C[e][e] {};
        int set[w];
        for (int l = 0; l < e; l++) {
            memcpy(set, x[l], sizeof(x[l]));
            for (int r = l; r < e; r++)
                for (int iw = 0; iw < w; iw++) {
                    set[iw] = min(set[iw], x[r][iw]);
                    C[l][r] += set[iw];
                }
        }

        int dp[e][e];
        fill(*dp, *dp + e * e, MAX);
        for (int i = 0; i < e; i++)
            dp[i][i] = 0;
        for (int s = 1; s < e; s++)
            for (int l = 0; l < e - s; l ++) {
                int r = l + s;
                for (int x = l; x < r; x++) {
                    dp[l][r] = min(dp[l][r], dp[l][x] + 2 * (C[l][x] - C[l][r]) + dp[x + 1][r] + 2 * (C[x + 1][r] - C[l][r]));
                }
            }

        cout << "Case #" << it << ": " << dp[0][e - 1] + 2 * C[0][e - 1] << endl;
    }
    return 0;
}
