import java.io.*;
import java.util.Scanner;
import java.math.*;
public class Solution {
    public static void main(String args[] ) throws Exception {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT */
        Scanner in= new Scanner(System.in);
        int x = Integer.parseInt(in.nextLine());
        for(int i = 1; i<=x; i++)
            {
            String[] z = in.nextLine().split(" ");
            long n1 = Long.parseLong(z[0]); 
            long n2 = Long.parseLong(z[1]); 
            System.out.println( (long) (Math.floor(Math.sqrt(n2)) - Math.ceil(Math.sqrt(n1)) + 1));
            
        }
    }
}