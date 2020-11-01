#include <iostream>
using namespace std;

int main() {
    int t, n, k, p, beauty;
    cin >> t;
    for (int c = 1; c <= t; ++c) {
        cin >> n >> k >> p;
        int sum[n][k + 1];
        for (int i = 0; i < n; ++i) {
            sum[i][0] = 0;
            for (int j = 0; j < k; ++j) {
                cin >> beauty;
                sum[i][j + 1] = sum[i][j] + beauty;
            }
        }
        int dp[n + 1][p + 1];
        fill(*dp, *dp + (n + 1) * (p + 1), 0);
        for (int i = 1; i < n + 1; ++i) {
            for (int j = 0; j < p + 1; ++j) {
                for (int x = 0; x < min(j,k) + 1; ++x) {
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - x] + sum[i - 1][x]);
                }
            }
        }
        cout << "Case #" << c << ": " << dp[n][p] << endl;
    }
}