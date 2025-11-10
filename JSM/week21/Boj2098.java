package cglab_JSM.JSM.week21;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Boj2098 {
    static int N;                       // 도시 개수
    static int[][] W;                   // 도시 간 이동비용 행렬
    static int[][] dp;                  // DP
    static int statusFullBit;           // 모든 도시 방문 상태(111...1)
    static final int INF = 100000000;   // 충분히 큰 값(경로가 없는 경우 처리용)


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());    // 도시 개수 입력

        // 비용 입력
        W = new int[N][N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                W[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        statusFullBit = (1 << N) - 1;   // (모든 도시 방문 상태)
        dp = new int[N][statusFullBit]; // dp[now][visited]: 지금 now 도시에 있고, visited 상태일 때 남은 모든 도시를 방문하고 출발점(0번)으로 돌아가는 최소비용
        for (int[] row : dp) Arrays.fill(row, -1);  // -1로 초기화(아직 계산 안 함 표시)

        System.out.println(tsp(0, 1));  // 0번 도시에서 시작 (0001: 0번도시 방문상태)
    }

    static int tsp(int now, int visited) {
        // 모든 도시를 방문한 경우
        if (visited == statusFullBit) {
            // 출발 도시 0번으로 돌아갈 수 있으면 비용 반환
            return (W[now][0] != 0) ? W[now][0] : INF;
        }

        if (dp[now][visited] != -1) {
            return dp[now][visited];
        }

        dp[now][visited] = INF;

        // 다음 도시 탐색
        for (int next = 0; next < N; next++) {
            // 경로 없거나 이미 방문한 도시면 패스
            if (W[now][next] == 0 || (visited & (1 << next)) != 0) continue;

            // 재귀함수
            int cost = tsp(next, visited | (1 << next)) + W[now][next];
            dp[now][visited] = Math.min(dp[now][visited], cost);
        }

        return dp[now][visited];
    }
}
