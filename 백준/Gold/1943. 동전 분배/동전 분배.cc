#include <iostream>
#include <vector>
using namespace std;

bool can_split_equally(int N, vector<pair<int, int>>& coins) {
    int total = 0;
    for(auto& coin : coins) {
        total += coin.first * coin.second;
    }
    
    if(total % 2 != 0) return false;
    
    int target = total / 2;
    vector<bool> dp(target + 1, false);
    dp[0] = true;
    
    for(auto& coin : coins) {
        int value = coin.first;
        int count = coin.second;
        
        for(int sum = target; sum >= 0; sum--) {
            if(dp[sum]) {
                for(int i = 1; i <= count && sum + value * i <= target; i++) {
                    dp[sum + value * i] = true;
                }
            }
        }
    }
    
    return dp[target];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int T = 3;  // 테스트 케이스 수
    while(T--) {
        int N;
        cin >> N;
        
        vector<pair<int, int>> coins(N);  // {value, count}
        for(int i = 0; i < N; i++) {
            cin >> coins[i].first >> coins[i].second;
        }
        
        cout << (can_split_equally(N, coins) ? 1 : 0) << '\n';
    }
    
    return 0;
}