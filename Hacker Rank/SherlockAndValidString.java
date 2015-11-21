
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc  = new Scanner(System.in);
        String retval = "NO";
        String m = sc.nextLine();
        HashMap<Character,Integer> map = new HashMap<Character,Integer>();
        for(int i=0;i<m.length();i++)
        {
            if(map!=null && !map.containsKey(m.charAt(i)))
                {
                map.put(m.charAt(i),1);
            }
            else
                {
                 map.put(m.charAt(i),map.get(m.charAt(i))+1);
            }
        }
  
        if(checkAllValuesEqual(map))
         {
            retval = "YES";
        }
        else
        {
         for(char key : map.keySet())
        {
            map.put(key,map.get(key)-1);
            if(checkAllValuesEqual(map))
                {
                  retval = "YES";
                    break;
             }
             else
                 {
                 map.put(key,map.get(key)+1);
             }
        }
      
       }
           System.out.println(retval);   
    }
    public static boolean checkAllValuesEqual(HashMap<Character, Integer> mapper)
        {
        Set<Integer> values = new HashSet<Integer>(mapper.values());
                values.remove(0);
        boolean isUnique = values.size() == 1;

        return isUnique;
    }
}
