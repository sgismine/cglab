import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main {

    static int N, M;
    static char[][] miro;
    static int[][] dist;
    static int[] dx = {1, 0, -1, 0}; // 하, 우, 상, 좌
    static int[] dy = {0, 1, 0, -1};
    public static class Pair{
        int x,y;
        public Pair(int x, int y){
            this.x =x;
            this.y =y;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        
         N = Integer.parseInt(st.nextToken()); // 세로
         M = Integer.parseInt(st.nextToken()); // 가로


        miro = new char[N][M];
        dist = new int[N][M];

        Queue<Pair> queue = new LinkedList<>();

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                miro[i][j] = line.charAt(j);
                dist[i][j] = -1; //방문하지 않은 칸은 -1
            }
        }

        bfs(0,0);

        // 결과 출력
        System.out.println(dist[N - 1][M - 1] + 1);

    }

    public static void bfs(int x, int y){
        Queue<Pair> queue = new LinkedList<>();
        queue.offer(new Pair(x,y));
        dist[x][y] =0;

        while(!queue.isEmpty()){
            Pair p =queue.poll();

            for(int i=0; i<4;i++){
                int nx =p.x + dx[i];
                int ny = p.y + dy[i];

                if (nx < 0 || ny < 0 || nx >= N || ny >= M) continue;
                if (miro[nx][ny] == '0' || dist[nx][ny] != -1) continue;

                queue.offer(new Pair(nx, ny));
                dist[nx][ny] = dist[p.x][p.y] + 1;
            }
        }
    }
}