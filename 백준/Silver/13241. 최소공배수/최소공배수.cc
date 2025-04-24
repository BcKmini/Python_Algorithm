#include <iostream>
using namespace std;

long long gcd(long long a, long long b) {
    while (b != 0) {
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main() {
    long long A, B;
    cin >> A >> B; 

    long long g = gcd(A, B);
    long long lcm = (A / g) * B;

    cout << lcm;
    return 0;
}