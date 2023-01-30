/*
 * Kudos to AwakeAnay for the solution
 * https://codingcompetitions.withgoogle.com/kickstart/submissions/00000000008cb4d1/000000000065d150
*/

#include <iostream>

#define int long long

const int MOD = 1000'000'007;

const int MAXN = 405;

int binom[MAXN][MAXN];

int expo(int x, int p) {
  int ret = 1;
  while(p > 0) {
    if(p&1)
      ret = (ret*x)%MOD;
    p >>= 1;
    x = (x*x)%MOD;
  }
  return ret;
}

int inv(int x) {
  return expo(x, MOD-2);
}

int dp[MAXN][MAXN][MAXN];

signed main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(0);

  for(int i = 0; i < MAXN; i++)
    binom[i][0] = binom[i][i] = 1;

  for(int i = 0; i < MAXN; i++)
    for(int j = 1; j < i; j++)
      binom[i][j] = (binom[i-1][j] + binom[i-1][j-1])%MOD;

  int T;
  std::cin >> T;

  for(int t = 1; t <= T; t++) {
    std::cout << "Case #" << t << ": ";

    int n;
    std::cin >> n;

    std::string s;
    std::cin >> s;

    for(int i = 0; i < n; i++) {
      for(int j = 0; j < n; j++) {
        dp[1][i][j] = std::max(0ll, j-i+1);
        dp[0][i][j] = 1;
      }
    }

    for(int i = 2; i <= n; i++) {
      for(int j = 0; j < n; j++)
        for(int k = 0; k < n; k++)
          dp[i][j][k] = 0;

      for(int j = 2; j <= n; j++) {
        for(int u = 0; u+j <= n; u++) {
          int v = u+j-1;
          dp[i][u][v] = (dp[i][u+1][v] + dp[i][u][v-1] - dp[i][u+1][v-1] + MOD)%MOD;
          if(s[u] == s[v])
            dp[i][u][v] = (dp[i][u][v] + dp[i-2][u+1][v-1])%MOD;
        }
      }
    }

    int ans = 0;
    for(int i = 0; i < n; i++) {
      ans += dp[i][0][n-1]*inv(binom[n][i]);
      ans %= MOD;
    }

    std::cout << ans;

    std::cout << std::endl;
  }

  return 0;
}

