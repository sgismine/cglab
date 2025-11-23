package cglab_JSM.JSM.week24;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

public class Boj2164 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Queue<Integer> queue = new ArrayDeque<>();

        int N = Integer.parseInt(br.readLine());

        for (int i = 1; i <= N; i++) {
            queue.offer(i);
        }

        boolean flag = false;

        while (queue.size() > 1) {
            if (!flag) {
                queue.poll();
            } else {
                queue.offer(queue.poll());
            }
            flag = !(flag);
        }

        System.out.println(queue.peek());

    }
}
