package LinkedList;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {

    private static class Node {
        char value;
        Node prev;
        Node next;

        Node(char value) {
            this.value = value;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testCase = Integer.parseInt(br.readLine());
        for (int i = 0; i < testCase; i++) {
            Node head = new Node('\0');
            Node tail = new Node('\0');
            head.next = tail;
            tail.prev = head;
            Node cursor = tail;

            String initial = br.readLine();
            for (char ch : initial.toCharArray()) {
                switch (ch) {
                    case '<':
                        if (cursor.prev != head) {
                            cursor = cursor.prev;
                        }
                        break;
                    case '>':
                        if (cursor != tail) {
                            cursor = cursor.next;
                        }
                        break;
                    case '-':
                        Node toDelete = cursor.prev;
                        if (toDelete != head) {
                            Node prevNode = toDelete.prev;
                            prevNode.next = cursor;
                            cursor.prev = prevNode;
                        }
                        break;
                    default:
                        Node newNode = new Node(ch);
                        Node prev = cursor.prev;
                        prev.next = newNode;
                        newNode.prev = prev;
                        newNode.next = cursor;
                        cursor.prev = newNode;
                        break;
                }
            }

            StringBuilder sb = new StringBuilder();
            Node current = head.next;
            while (current != tail) {
                sb.append(current.value);
                current = current.next;
            }
            System.out.println(sb);
        }
    }
}
