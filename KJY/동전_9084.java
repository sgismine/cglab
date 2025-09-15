package DP;

import java.util.Scanner;

public class 동전_9084 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt(); // 테스트 케이스의 개수

        while (T-- > 0) {
            int N = sc.nextInt(); // 동전의 가지 수
            int[] coins = new int[N];
            for (int i = 0; i < N; i++) {
                coins[i] = sc.nextInt();
            }
            int M = sc.nextInt(); // 목표 금액

            // dp[i]는 금액 i를 만드는 방법의 수를 저장
            int[] dp = new int[M + 1];
            dp[0] = 1; // 금액 0을 만드는 방법은 1가지

            // 각 동전의 종류를 순회
            for (int coin : coins) {
                // 현재 동전을 사용하여 금액을 채워나감
                for (int i = coin; i <= M; i++) {
                    dp[i] += dp[i - coin];
                }
            }
            System.out.println(dp[M]);
        }
        sc.close();
    }
}
