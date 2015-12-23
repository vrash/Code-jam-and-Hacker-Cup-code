/*

Bob is in a candy shop and wants to purchase his favorite candy, which he knows costs N dollars. He has an infinite number of 1,2,5,10,20,50, and 100 dollar bills in his pocket. Bob wants to know the number of different ways he can pay the N dollars for his candy.

Input Format

A single integer, N, which is the cost of Bob's candy.

Constraint
1≤N≤250

Output Format

Print an integer representing the number of different variations of how Bob can pay.
*/
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        // your code goes here
        int[] coins = {1,2,5,10,20,50,100};
        int[] ways = new int[N+1];
        ways[0] = 1;
        for(int i=0; i< coins.length; i++)
            {
            for(int j=coins[i];j<=N;j++)
                {
                ways[j] = ways[j]+ ways[j-coins[i]];
            }
        }
        System.out.println(ways[ways.length-1]);
        
    }
}
