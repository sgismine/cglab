import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        
        Stack<Integer> inputStack = new Stack<>();
        for (int i = 0; i < N; i++) {
            inputStack.push(Integer.parseInt(st.nextToken()));
        }
        Stack<Integer> candStack = new Stack<>();
        Stack<Integer> resultStack = new Stack<>();


        while (!inputStack.isEmpty()) {
            int cur = inputStack.pop();
            while (!candStack.isEmpty() && candStack.peek() <= cur) {
                candStack.pop();
            }


            if (candStack.isEmpty()) {
                resultStack.push(-1);
            } else {
                resultStack.push(candStack.peek());
            }


            candStack.push(cur);
        }
        
        StringBuilder sb = new StringBuilder();
        while (!resultStack.isEmpty()) {
            sb.append(resultStack.pop()).append(' ');
        }

        System.out.println(sb.toString());
    }
}