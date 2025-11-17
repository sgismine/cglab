package cglab_JSM.JSM.week23;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Boj17298 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());        // 수열 크기 입력

        int[] arr = new int[N];                         // 수열 넣을 배열
        int[] NGE = new int[N];                         // 오큰수 넣을 배열

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());  // 수열 채우기
            NGE[i] = -1;                                // 오큰수 -1로 초기화
        }


        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < N; i++) {
            while (!(stack.empty()) && (arr[stack.peek()] < arr[i])) {  // 스택이 빈 공간이 아니고 i번째 수가 그 전 수보다 크면
                NGE[stack.pop()] = arr[i];                              // 그 전 수의 오큰수가 arr의 i번째 수가 된다.
            }
            stack.push(i);                              // arr[i]의 index를 stack에 저장
        }

        StringBuilder sb = new StringBuilder();
        for (int num : NGE) {
            sb.append(num).append(" ");
        }

        System.out.println(sb);
    }
}
