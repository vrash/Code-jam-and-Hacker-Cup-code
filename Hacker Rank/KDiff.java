import java.io.*;
import java.util.Scanner;
import java.util.HashSet;
public class Solution {
    public static void main(String args[] ) throws Exception {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT */
        Scanner in = new Scanner(System.in);
        String[] inputter = in.nextLine().split(" ");
        int N = Integer.parseInt(inputter[0]);
        int K = Integer.parseInt(inputter[1]);
        int i = 0;
        String[] input = in.nextLine().split(" ");
        long[] arr = new long[N];
        HashSet<Long> map = new HashSet<Long>();
        for(String elem: input)
            {
            arr[i]=Long.parseLong(elem);
            map.add(arr[i]);
            i++;
        }
        int count =0;
        for(i=0;i<arr.length;i++)
            {
            if(map.contains(arr[i]+K))
                count++;
            }
        System.out.println(count);
    }
}