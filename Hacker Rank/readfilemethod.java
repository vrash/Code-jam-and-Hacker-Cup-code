public static void readFileByLine(String fileName) {
  try {
   File file = new File(fileName);
   Scanner scanner = new Scanner(file);
   while (scanner.hasNext()) {
    System.out.println(scanner.next());
   }
   scanner.close();
  } catch (FileNotFoundException e) {
   e.printStackTrace();
  } 
 }