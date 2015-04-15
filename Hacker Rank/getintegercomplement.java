 static int getIntegerComplement(int n) {

    int ones = (Integer.highestOneBit(n) << 1) - 1;
    return n ^ ones;
    }
