package cglab_JSM.JSM.week22;

import java.io.*;
import java.util.LinkedList;
import java.util.ListIterator;

public class Boj1406 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        LinkedList<Character> list = new LinkedList<>();    // 문자들 저장할 리스트
        int M;
        String order;
        ListIterator<Character> iterator;   // 커서 역할

        // LinkedList 초기화 (문자열 한 문자씩 list에 저장)
        String str = br.readLine();
        for(int i=0; i < str.length(); i++)
            list.add(str.charAt(i));

        // 명령어 개수 입력
        M = Integer.parseInt(br.readLine());

        //시작점은 list의 마지막 (커서 위치를 문자열의 맨 끝으로 이동)
        iterator = list.listIterator(list.size());

        // M개의 명령어 처리
        for(int i=0; i < M; i++){
            order = br.readLine();

            switch (order.charAt(0)){
                case 'L': // 왼쪽으로 한 칸
                    if(iterator.hasPrevious()) // 앞이 있으면 이동
                        iterator.previous();
                    break;

                case 'D': // 오른쪽으로 한 칸
                    if(iterator.hasNext()) // 뒤가 있으면 이동
                        iterator.next();
                    break;

                case 'B': // 앞 글자 삭제
                    if(iterator.hasPrevious()){ // 앞이 있는지 확인
                        iterator.previous(); // 앞으로 이동
                        iterator.remove(); // 삭제시킴
                    }
                    break;

                case 'P':
                    iterator.add(order.charAt(2)); // 글자 넣기
                    break;
            }
        }

        iterator = list.listIterator(); // 처음으로 커서 돌리기 위해 새로 지정
        while(iterator.hasNext())
            bw.write(iterator.next());
        bw.flush();
        bw.close();
    }
}
