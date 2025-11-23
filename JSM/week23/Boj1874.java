package cglab_JSM.JSM.week23;

import java.util.Scanner;
import java.util.Stack;

public class Boj1874 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();                   // 수 개수
        int[] arr = new int[n];                 // 만들 수열 저장할 곳

        for (int i = 0; i < n; i++) {           // 수 입력
            arr[i] = sc.nextInt();
        }

        Stack<Integer> stack = new Stack<>();
        StringBuilder sb = new StringBuilder();

        int num = 1;                            // stack에 넣을 수 (1~n)
        int index = 0;                          // 내가 뽑아야할 수 위치 알려줌

        // 모든 원소 순서대로 만들 때까지 반복
        while (index < n) {
            if (num <= arr[index]) {            // 뽑아야할 수 나올 때까지 push()
                stack.push(num++);
                sb.append("+\n");
            } else {
                if (stack.peek() == arr[index]) {   // 뽑아야할 수 나오면 pop()
                    stack.pop();
                    sb.append("-\n");
                    index++;
                } else {                            // 뽑아야할 수 없으면 종료
                    System.out.println("NO");
                    return;
                }
            }
        }
        System.out.println(sb);
        sc.close();
    }
}
