package Stack;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        Stack<Integer> stack = new Stack<>();

        int current = 1;
        boolean isPossible = true;

        for (int i = 0; i < n; i++) {
            int target = Integer.parseInt(br.readLine());

            while (current <= target) {
                stack.push(current++);
                sb.append("+\n");
            }

            if (!stack.isEmpty() && stack.peek() == target) {
                stack.pop();
                sb.append("-\n");
            } else {
                isPossible = false;
                break;
            }
        }

        if (isPossible) {
            System.out.println(sb);
        } else {
            System.out.println("NO");
        }

    }
}
