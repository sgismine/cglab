package cglab_JSM.JSM.week23;

import java.util.Scanner;
import java.util.Stack;

public class Boj10773 {
    public static void main(String[] args) {

        Stack<Integer> stack = new Stack<>();

        Scanner sc = new Scanner(System.in);
        int K = sc.nextInt();                   // 개수 입력
        int sum = 0;                            // 합

        for (int i = 0; i < K; i++) {
            int num = sc.nextInt();             // 수 입력
            if (num == 0) {                     // 입력 0 이면
                if ((!stack.empty()))           // 스택 안 비어있으면
                    sum -= stack.pop();         // 합에서 빼고 삭제
            } else {                            // 입력 0 아니면
                sum += stack.push(num);         // 합에 더하면서 push()
            }
        }

        System.out.println(sum);
        sc.close();
    }
}