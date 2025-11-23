package cglab_JSM.JSM.week24;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Boj18258 {

    static int[] queue = new int[2000000];

    static int first = 0;
    static int last = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int cmd = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < cmd; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String S = st.nextToken();

            switch(S) {
                case "push" :
                    push(Integer.parseInt(st.nextToken()));
                    break;
                case "pop" :
                    sb.append(pop()).append("\n");
                    break;
                case "size" :
                    sb.append(size()).append("\n");
                    break;
                case "empty" :
                    sb.append(empty()).append("\n");
                    break;
                case "front" :
                    sb.append(front()).append("\n");
                    break;
                case "back" :
                    sb.append(back()).append("\n");
                    break;
            }
        }
        System.out.println(sb);
    }

    public static void push(int X) {
        queue[last] = X;
        last++;
    }

    public static int pop() {
        if(last - first == 0) {
            return -1;
        } else {
            return queue[first++];
        }
    }

    public static int size() {
        return last - first;
    }

    public static int empty() {
        if(last - first == 0) {
            return 1;
        } else {
            return 0;
        }
    }

    public static int front() {
        if(last - first == 0) {
            return -1;
        } else {
            return queue[first];
        }
    }

    public static int back() {
        if(last - first == 0) {
            return -1;
        }else {
            return queue[last - 1];
        }
    }
}
