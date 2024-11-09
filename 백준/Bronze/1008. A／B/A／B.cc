#include <iostream>
#include <iomanip>  // 소수점 출력을 위해 필요한 헤더 파일

int main() {
    // 변수 선언
    int A, B;

    // 두 정수 A와 B를 입력 받기
    std::cin >> A >> B;

    // A/B의 결과를 계산
    double result = static_cast<double>(A) / B;

    // 소수점 아래 10자리까지 출력
    std::cout << std::fixed << std::setprecision(10) << result << std::endl;

    return 0;
}
