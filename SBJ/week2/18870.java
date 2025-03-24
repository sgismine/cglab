import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
//import java.util.ArrayList;
//import java.util.Arrays;
//import java.util.Collections;
//import java.util.List;

//시간 초과 (이분 탐색이나 Hash로 풀이 할 것)
class Main {
    public static void main(String[] args) throws IOException {
        // 코드 작성
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
         StringBuilder sb = new StringBuilder();
         int N = Integer.parseInt(br.readLine());
         String[] input = br.readLine().split(" ");
         int[] arr = new int[N];
         //배열 생성
         for (int i = 0; i < arr.length; i++) {
             arr[i] = Integer.parseInt(input[i]);
            }//end for

        // int[] resultArr = new int[N];
        // for (int i = 0; i < arr.length; i++) {
        //         int count =0;
        //     for (int j = 0; j < arr.length; j++) {
        //             if(arr[i]>arr[j]){
        //             count++;
        //         }
        //     }
        //         resultArr[i]=count;
        // }//end for

        

        for(Integer output:resultArr){
            sb.append(output).append(" ");
        }
        System.out.println(sb);
            
    }
}