import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.StringTokenizer;

class Main {
    static int N,M;

    static int[] cntOfLink;
    static ArrayList<ArrayList<Integer>> graph;
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        cntOfLink = new int[N+1]; //간선의 갯수


        graph = new ArrayList<>(N+1);
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<Integer>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());

            graph.get(v1).add(v2);
            cntOfLink[v2]++; //진입 차수 계산
        }

        KahnSort();
    
    }

    static void KahnSort() {
        Deque<Integer> q = new ArrayDeque<>();
        for (int i = 1; i <= N; i++) {
            if(cntOfLink[i] ==0) q.addLast(i);
        }

        StringBuilder sb = new StringBuilder();
        int processed = 0;
        while(!q.isEmpty()){
            int cur = q.removeFirst();
            sb.append(cur).append(' ');
            processed++;
            for (int nxt : graph.get(cur)) {
                if (--cntOfLink[nxt] == 0) q.addLast(nxt);
            }
        }

        if (processed < N) {
            // 사이클이 있어서 위상 정렬 불가
            System.out.println("cycle detected");
            return;
        }

        System.out.println(sb.toString().trim());
    }
}