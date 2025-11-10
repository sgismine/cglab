package cglab_JSM.JSM.week22;

import java.io.*;
import java.util.LinkedList;
import java.util.ListIterator;

public class Boj5397 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 테스트 문자열 개수
        int testCount = Integer.parseInt(br.readLine());

        while (testCount-- > 0) {
            String testString = br.readLine();
            LinkedList<Character> list = new LinkedList<>();    // 입력된 문자들 저장할 리스트
            ListIterator<Character> iterator = list.listIterator();

            for (char c : testString.toCharArray()) {
                switch (c) {
                    case '<':
                        if (iterator.hasPrevious()) {
                            iterator.previous();
                        }
                        break;
                    case '>':
                        if (iterator.hasNext()) {
                            iterator.next();
                        }
                        break;
                    case '-':
                        if (iterator.hasPrevious()) {
                            iterator.previous();
                            iterator.remove();
                        }
                        break;
                    default:
                        iterator.add(c);
                        break;
                }
            }

            iterator = list.listIterator(); // 처음으로 커서 돌리기 위해 새로 지정
            while(iterator.hasNext())
                bw.write(iterator.next());

            bw.write('\n');
        }
        bw.flush();
        bw.close();
        br.close();
    }
}
