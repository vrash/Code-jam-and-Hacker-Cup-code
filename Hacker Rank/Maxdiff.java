
    static int maxDifference(int[] a) {
         int maxDiff = -1;
         int minElem = a[0];
        for(int i=1;i<a.length;i++)
            {
            if((a[i]-minElem)>maxDiff)
                maxDiff = a[i]-minElem;
            if(a[i]<minElem)
                minElem = a[i];
        }
         return maxDiff;

    }