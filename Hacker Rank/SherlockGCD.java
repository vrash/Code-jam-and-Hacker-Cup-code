import java.util.Scanner;
import java.util.ArrayList;
 
public class Solution{
    public static void main(String[] args){
        Scanner reader = new Scanner(System.in);
        int T =reader.nextInt();
        for(int i=0;i<T;i++){
            int N = reader.nextInt();
            int[] a = new int[N];
            int gc = 0;
            for(int j=0;j<N;j++){
                a[j] = reader.nextInt();
                gc = gcd(gc,a[j]);
            }
            if(gc==1)
                System.out.println("YES");
            else
                System.out.println("NO");
        }
    }
     
    static int gcd(int m, int n){
        while(n>0){
            int tmp = n;
            n = m % n;
            m = tmp;
        }
        return m;
    }
}