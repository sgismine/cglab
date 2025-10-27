package cglab_JSM.JSM.week21;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Boj2253 {
    static final int INF = 1000000;
    static int N, M;
    static boolean[] isSmall;     // 작은 돌 여부
    static int[][] dp;              // dp[i][k]: 'i번 돌에 점프 길이 k'로 도착했을 때의 최소 점프 횟수

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 첫 줄 N, M 입력
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        // 작은 돌 입력
        isSmall = new boolean[N + 1];
        for (int i = 0; i < M; i++) {
            int b = Integer.parseInt(br.readLine());
            isSmall[b] = true;
        }

        // 점프 길이 최대 범위 설정
        int maxJump = (int) Math.sqrt(2 * N) + 2;
        dp = new int[N + 1][maxJump + 1];
        for (int i = 0; i <= N; i++) Arrays.fill(dp[i], INF);

        // 시작점: 1번 돌, 아직 점프 안 함
        dp[1][0] = 0;

        // DP 탐색
        for (int i = 1; i <= N; i++) {
            if (isSmall[i]) continue; // 작은 돌은 건너뜀

            for (int k = 0; k < maxJump; k++) {
                if (dp[i][k] == INF) continue;

                // 다음 점프 길이 후보: k-1, k, k+1
                for (int nextK = k - 1; nextK <= k + 1; nextK++) {
                    if (nextK <= 0) continue;   // 점프 길이 > 0
                    int next = i + nextK;
                    if (next <= N && !isSmall[next]) {
                        dp[next][nextK] = Math.min(dp[next][nextK], dp[i][k] + 1);  // 더 작으면 갱신
                    }
                }
            }
        }

        // N번 돌에 도착 가능한 모든 점프 길이 중 최소 횟수 찾기
        int ans = INF;
        for (int k = 1; k <= maxJump; k++) {
            ans = Math.min(ans, dp[N][k]);
        }

        // 출력
        System.out.println(ans == INF ? -1 : ans);

    }
}
