
    static String isitpossible(int a, int b, int c, int d) {
        
        if(a==c && b==d)
            return "Yes";
        while(!(a==c && b==d) && Math.abs(c-d)>0)
            {
            if(c>d)
             c-=d;   
            else
             d-=c;
        }
        //System.out.println(a+" "+b+" "+c+" "+d+"");
         if(a==c && b==d)
            return "Yes";
        else 
            return "No";
    }