package cglab_JSM.JSM.week22;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.StringTokenizer;

public class Boj1158 {
    public static void main(String[] args) throws IOException {
        LinkedList<Integer> list = new LinkedList<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());   // 총 인원 수
        int K = Integer.parseInt(st.nextToken());   // 제거되는 순서


        for (int i = 1; i <= N; i++) {
            list.add(i);
        }

        ListIterator<Integer> iterator = list.listIterator();

        StringBuilder sb = new StringBuilder();
        sb.append("<");

        while (!(list.isEmpty())) {
            for (int i = 0; i < K; i++) {
                if (!(iterator.hasNext())) {
                    iterator = list.listIterator();
                }
                if (i == K-1) {
                    sb.append(iterator.next());
                    iterator.remove();
                    if (!list.isEmpty()) sb.append(", ");
                }
                else {
                    iterator.next();
                }
            }
        }

        sb.append(">");

        System.out.println(sb);

        br.close();
    }
}
