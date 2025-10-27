package cglab_JSM.JSM.week20;

import java.util.Scanner;

public class Boj11053 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] A = new int[N];
        int[] dp = new int[N];

        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }

        int result = 0;

        for (int i = 0; i < N; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {                   // A[j] < A[i] (j < i) 라면, A[j]를 마지막으로 하는 LIS 뒤에 A[i]를 붙일 수 있음.
                if (A[j] < A[i]) {                          // 그럼 LIS의 길이는 dp[j] + 1
                    dp[i] = Math.max(dp[i], dp[j] + 1);     // A[j] < A[i] (j < i) 라도 +1하면 안 되는 경우, 기존 dp[i]를 가져감.
                }
            }
            result = Math.max(result, dp[i]);
        }

        System.out.println(result);
        sc.close();
    }

    // A[j] < A[i] (j < i) 라면, A[j]를 마지막으로 하는 LIS 뒤에 A[i]를 붙일 수 있음.
    // 그럼 LIS의 길이는 dp[j] + 1
    // A[j] < A[i] (j < i) 라도 +1하면 안 되는 경우, 기존 dp[i]를 가져감.
}
