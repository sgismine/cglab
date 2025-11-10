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

        // Doubly-linked list with sentinels to support O(1) cursor edits.
        Node head = new Node('\0');
        Node tail = new Node('\0');
        head.next = tail;
        tail.prev = head;
        Node cursor = tail; // cursor points to the node immediately right of the caret.

        String initial = br.readLine();
        for (char ch : initial.toCharArray()) {
            Node newNode = new Node(ch);
            Node prev = tail.prev;
            prev.next = newNode;
            newNode.prev = prev;
            newNode.next = tail;
            tail.prev = newNode;
        }

        int commandCount = Integer.parseInt(br.readLine());
        for (int i = 0; i < commandCount; i++) {
            String line = br.readLine();
            char command = line.charAt(0);

            switch (command) {
                case 'L':
                    if (cursor.prev != head) {
                        cursor = cursor.prev;
                    }
                    break;
                case 'D':
                    if (cursor != tail) {
                        cursor = cursor.next;
                    }
                    break;
                case 'B':
                    Node toDelete = cursor.prev;
                    if (toDelete != head) {
                        Node prevNode = toDelete.prev;
                        prevNode.next = cursor;
                        cursor.prev = prevNode;
                    }
                    break;
                case 'P':
                    Node newNode = new Node(line.charAt(2));
                    Node prevNode = cursor.prev;
                    prevNode.next = newNode;
                    newNode.prev = prevNode;
                    newNode.next = cursor;
                    cursor.prev = newNode;
                    break;
                default:
                    break;
            }
        }

        StringBuilder sb = new StringBuilder();
        Node current = head.next;
        while (current != tail) {
            sb.append(current.value);
            current = current.next;
        }

        System.out.print(sb);
    }
}
