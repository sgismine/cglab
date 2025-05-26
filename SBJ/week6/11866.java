import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main {
    public static Queue<Integer> q = new LinkedList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        for (int i = 1; i <= N; i++) {
            q.add(i);
        }
        StringBuilder sb = new StringBuilder();
        sb.append("<");
        while (q.size() != 0){
                sb.append(Josephus(q,K));
                if(!q.isEmpty()){
                    sb.append(", ");
                }
        }
        sb.append(">");

        System.out.println(sb);
    }

    private static Integer Josephus(Queue<Integer> q, int K) {
        for (int i = 1; i < K; i++) {
            int head = (int) q.poll(); //제일 위의 값을 반환하고 삭제제
            q.offer(head); // 제일 위의 값을 제일 밑에 붙이기
        }
    
        return q.remove();
    }
}