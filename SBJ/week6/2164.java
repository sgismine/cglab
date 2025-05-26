import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

class Main {
    public static Queue<Integer> q = new LinkedList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());    
    
        for (int i = 1; i <= N; i++) {
            q.add(i);
        }

        while (q.size() != 1){
            Card(q);
        }
        System.out.println(q.element()); //가장 위의 값을 반환환
    }

    public static void Card (Queue<Integer> q ){
        q.remove(); // 제일 위의 값을 삭제
        int head = (int) q.poll(); //제일 위의 값을 반환하고 샂게
        q.offer(head); // 제일 위의 값을 제일 밑에 붙이기
    }
}