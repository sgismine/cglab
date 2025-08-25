import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

class Main {
    static class Node{
        int z;
        int x;
        int y;
        public Node(int z, int x, int y){
            this.z=z;
            this.x=x;
            this.y=y;
            
        }
    }

    public static int M,N,H;
    public static int[][][] tomato;

    public static int[] dx = {-1,1,0,0,0,0};
    public static int[] dy = {0,0,-1,1,0,0};
    public static int[] dz = {0,0,0,0,-1,1};

    public static ArrayDeque<Node> q =  new ArrayDeque<>();
    static int unripe= 0;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader((new InputStreamReader(System.in)));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        tomato = new int[H][N][M];
        for(int h = 0; h<H;h++){
            for( int n =0; n<N;n++){
                st = new StringTokenizer(br.readLine());
                for( int m =0;m<M;m++){
                    tomato[h][n][m] = Integer.parseInt(st.nextToken());
                    if(tomato[h][n][m] == 1){
                        q.offer(new Node(h,n,m)); //큐에 바로 넣기
                    }else if(tomato[h][n][m]==0){
                        unripe++;
                    }
                }
            }
        }

        int answer = bfs();
        System.out.println(answer);
    }

    public static int bfs(){
        if(unripe == 0) return 0; //다 익어있음
        
        int maxDay = 1; //초기 날짜를 1일

        while (!q.isEmpty()){
            Node cur = q.poll();

            int curDay = tomato[cur.z][cur.x][cur.y]; //현재 칸의 날짜

            for(int d =0; d<6;d++){
                int nz = cur.z +dz[d];
                int nx = cur.x + dx[d];
                int ny  = cur.y+dy[d];

                if(nz< 0 || nz >= H || nx<0 || nx >= N || ny <0|| ny >=M ) {
                    continue;
                }

                //전파 가능 여부 -> 안 익은 칸에만 전파
                if(tomato[nz][nx][ny]!=0){
                    continue;
                }

                //---------전파 성공 시------------
                //수행
                tomato[nz][nx][ny] = curDay+1;  // 하루 추가해서 저장

                unripe --;

                //최댓값 갱신
                if(tomato[nz][nx][ny] > maxDay){
                    maxDay = tomato[nz][nx][ny];
                }
                
                q.offer(new Node(nz,nx,ny));
            }
        }

        if(unripe>0) return -1;

        return maxDay -1;
    }
}