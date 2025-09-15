package DP;

import java.util.Scanner;

public class 피보나치수2_2748 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();

        // n이 0일 경우
        if (n == 0) {
            System.out.println(0);
            return;
        }

        // 피보나치 수를 저장할 배열 (long 타입)
        long[] fibo = new long[n + 1];

        // 초기값 설정
        fibo[0] = 0;
        fibo[1] = 1;

        // 반복문을 이용한 동적 계획법
        for (int i = 2; i <= n; i++) {
            fibo[i] = fibo[i - 1] + fibo[i - 2];
        }

        System.out.println(fibo[n]);
    }
}