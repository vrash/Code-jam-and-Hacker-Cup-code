import java.io.*;
import java.util.Scanner;
import java.math.*;
public class Solution {
     public static void main(String args[] ) throws Exception {
          /* Enter your code here. Read input from STDIN. Print output to STDOUT */
          Scanner sc = new Scanner(System.in);
          int T = Integer.parseInt(sc.nextLine());
          for(int i = 1;i<=T;i++)
              {
              BigInteger N = new BigInteger(sc.nextLine());
              solve(N);
          }
      }
      public static void solve(BigInteger N)
            {
            boolean louise=true;
            if(N.compareTo(BigInteger.ONE)==0)
                System.out.println("Richard");
            else{
            while(N.compareTo(BigInteger.ONE)==1)
                {
                if(!((N.and(N.subtract(BigInteger.ONE))).compareTo(BigInteger.ZERO)==0))
                   {
                  double doubleValue = Math.pow(2, Math.floor(Math.log(N.doubleValue()) / Math.log(2)));
                    //  System.out.println(doubleValue+"  "+N);
                  BigInteger diff = new BigDecimal(doubleValue).toBigInteger();
                    N=N.subtract(diff);
                    //  System.out.println(N);
                   }
                else
                   {
                   N = N.subtract(N.divide(new BigInteger("2")));
                   }
                  //System.out.println("HHH"+N);
                if((N.compareTo(BigInteger.ONE)==1))
                   louise=!louise;
            }
           if(louise)
                   System.out.println("Louise");
          else
                   System.out.println("Richard");
        }
        }
}