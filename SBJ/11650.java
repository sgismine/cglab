import java.io.IOException;
import java.util.Scanner;

class Main {
    public static void main(String[] args) throws IOException {
        // 코드 작성
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[][] arr = new int[N][2];

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < 2; j++) {
            arr[i][j] = scanner.nextInt();
        }
    }
    
    //삽입정렬을 이용하여 정렬
    for (int i = 1; i < arr.length; i++) {
        int j = i -1 ;
        int targetX = arr[i][0];
        int targetY = arr[i][1];
        while (j >=0 &&arr[j][0] > targetX ) {
            arr[j+1][0] = arr[j][0];
            arr[j+1][1] = arr[j][1];
            // if(arr[j][0] == targetX){
            //     if(arr[j+1][1] < arr[j][1]){
            //         arr[j+1][1] = arr[j][1];
            //     }
            // }
            j = j -1; 
        }
        arr[j+1][0] = targetX;
        arr[j+1][1] = targetY;
    }


    for (int i = 0; i < N; i++) {
        System.out.println(arr[i][0]+" "+arr[i][1]);
    }
        scanner.close();
    }
}