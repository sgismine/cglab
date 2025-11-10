package LinkedList;

import java.io.*;
import java.util.*;

class Main {

    static class Node {
        int data;
        Node next;
        Node(int data) {
            this.data = data;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        // 1. 원형 연결 리스트 생성
        Node head = new Node(1);
        Node prev = head;
        for (int i = 2; i <= N; i++) {
            Node node = new Node(i);
            prev.next = node;
            prev = node;
        }
        prev.next = head; // 마지막 노드가 첫 번째 노드를 가리키게 함 (원형 구조)

        // 2. 요세푸스 순열 생성
        StringBuilder sb = new StringBuilder();
        sb.append("<");

        Node current = prev; // 마지막 노드에서 시작 (이유: current.next가 첫 번째 노드)
        while (N-- > 0) {
            // K - 1번째 사람까지 이동
            for (int i = 0; i < K - 1; i++) {
                current = current.next;
            }

            // delete가 K번째 사람을 가리키고 있음
            Node delete = current.next;
            sb.append(delete.data);
            if (N > 0) sb.append(", ");

            // K번째 사람 제거
            // delete 노드를 리스트에서 제거하기 위해 delete 노드를 건너뜀
            current.next = delete.next;
        }

        sb.append(">");
        System.out.println(sb);
    }
}
