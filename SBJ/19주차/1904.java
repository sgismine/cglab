import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {

    public static int N;
    public static long[] table;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        //1,2를 사용하기 때문에  N+2해서 안전하게 사용 N+1를 사용할 시 런타임 에러
        //뭔가 topDown이 더 좋았을듯
        table = new long[N+2];
        
        System.out.println(bottomUp(N) %15746);
    }

    public static long bottomUp (int n){
        table[1] = 1;
        table[2] = 2;

        for(int i =3 ;i<=n;i++){
            table[i] = (table[i-1] + table[i-2]) % 15746 ;
        
        }

        return table[n];
    } 


}