package cglab_JSM.JSM.week23;

import java.util.Scanner;
import java.util.Stack;

public class Boj6198 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Stack<Integer> stack = new Stack<>();
        long sum = 0;                           // 최종 합
        int N = sc.nextInt();                   // 빌딩의 개수

        for (int i = 0; i < N; i++) {
            int h = sc.nextInt();               // 높이 입력

            while (!(stack.isEmpty())) {        // 스택 비어있다면
                if (stack.peek() <= h) {        // 새 높이가 이전 높이보다 크거나 같으면
                    stack.pop();                // pop(): h높이 빌딩을 볼 수 없으므로
                } else break;
            }
                                    // h높이 빌딩을 볼 수 있느냐를 판단 -> 못 보는 빌딩높이는 pop()해서 삭제함 -> stack.size()
            sum += stack.size();    // 0 / +1(10->3) / +1(10->7) / +2(10->4, 7->4) / 0 / +1(12->2)
            stack.push(h);          // push()
        }

        System.out.println(sum);
        sc.close();
    }
}
