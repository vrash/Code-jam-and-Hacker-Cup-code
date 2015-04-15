Set<Integer> union = new HashSet<Integer>(Arrays.asList(ID1));
union.addAll(Arrays.asList(ID2);

Set<Integer> intersection = new HashSet<Integer>(Arrays.asList(ID1));
intersection.retainAll(Arrays.asList(ID2);

union.removeAll(intersection);