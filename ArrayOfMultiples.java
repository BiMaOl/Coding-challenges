public class ArrayOfMultiples {
    public static int[] getList(int num, int len){
        int[] arr = new int[len];
        int sum = 0, i = 0;
        //multiplication loop: i times num
        while (i < len){ 
            sum += num; 
            arr[i++] = sum;
        }
        return arr;
    }
}