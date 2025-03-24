    import java.io.BufferedReader;
    import java.io.IOException;
    import java.io.InputStreamReader;
    //이거 안됨 퀵소트 최악의 경우 때문에 
    class Main {
        public static void main(String[] args) throws IOException {
            // 입력
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringBuilder sb = new StringBuilder();
            
            int N = Integer.parseInt(br.readLine());
            int[] arr = new int[N];
            
            // 입력 받기
            for (int i = 0; i < N; i++) {
                arr[i] = Integer.parseInt(br.readLine());
            }

            // 정렬 (QuickSort)
            QuickSort(arr, 0, N - 1);

            // 출력
            for (int i = 0; i < N; i++) {
                sb.append(arr[i]).append("\n");
            }
            System.out.print(sb);
        }

        // 퀵 정렬
        public static void QuickSort(int[] arr, int start, int end) {
            if (start < end) {
                int pivotIndex = partition(arr, start, end);
                QuickSort(arr, start, pivotIndex - 1);
                QuickSort(arr, pivotIndex, end);
            }
        }

        // 파티션 함수
        public static int partition(int[] arr, int start, int end) {
            int pivotValue = arr[(start + end) / 2];
            int left = start;
            int right = end;

            while (left <= right) {
                while (arr[left] < pivotValue) left++;
                while (arr[right] > pivotValue) right--;

                if (left <= right) {
                    int temp = arr[left];
                    arr[left] = arr[right];
                    arr[right] = temp;
                    left++;
                    right--;
                }
            }

            return left;
        }
    }
