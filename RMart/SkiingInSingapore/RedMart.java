import java.io.File;
import java.util.*;
public class RedMart {
   // public static int[][] example = new int[][]{{4, 8, 7, 3},{2, 5, 9, 3},{6, 3, 2, 5},{4, 4, 1, 6}};

    public static void main(String[] args)
    {
    	File file = new File("redmart.txt");
    	int[][] grid=null;
    	try{
    	Scanner sc = new Scanner(file);
    	String rcLine = sc.nextLine();

    	String[] rc = rcLine.split(" ");
    	int r = Integer.parseInt(rc[0]);
        int c =Integer.parseInt(rc[1]);
        grid = new int [r][c];
        System.out.println(r+","+c);
        for(int i=0;i<r;i++)
        { 
        	String rcLineDate = sc.nextLine();
        	String[] rcRowDataSplit = rcLineDate.split(" ");
        	
        	for(int j=0; j<c; j++)
        	{
        		grid[i][j] = Integer.parseInt(rcRowDataSplit[j]);
        	}
        }
    	}
    	catch(Exception ex)
    	{
    		System.err.println(ex.getMessage());
    	}
    	
    	RedMart finder = new RedMart(grid);
    	int[] answer = finder.find();
    	int size = answer.length;
    	int drop = (answer[0]-answer[answer.length-1]);
        System.out.println("Best overall: " + Arrays.toString(answer));
        System.out.println("Size: " + size);
        System.out.println("Drop: " + drop);
        System.out.println("Email to: " + size+drop+"@redmart.com");
    }

    private int[][] matrix;
    private PathInformation[][] informationForBestPathFromCellMemory;

    public RedMart(int[][] aMatrix)
    {
        informationForBestPathFromCellMemory = new PathInformation[aMatrix.length][];
        matrix = new int[aMatrix.length][];

        for(int i = 0; i < aMatrix.length; i++)
        {
            informationForBestPathFromCellMemory[i] = new PathInformation[aMatrix[i].length];
            matrix[i] = new int[aMatrix[i].length];

            for(int j = 0; j < aMatrix[i].length; j++)
            {
                matrix[i][j] = aMatrix[i][j];
            }
        }
    }
    public int[] find()
    {
        int currentBestStartingCellColumn = 0;
        int currentBestStartingCellRow = 0;
        for(int i = 0; i < matrix.length; i++)
        {
            for(int j = 0; j < matrix[i].length; j++)
            {
               if(getInformationForBestPathFromCell(i, j).compareTo(getInformationForBestPathFromCell(currentBestStartingCellColumn, currentBestStartingCellRow)) == 1){
                   currentBestStartingCellColumn = i;
                   currentBestStartingCellRow = j;
               }
            }
        }

        return unfoldBestPathFromCell(currentBestStartingCellColumn, currentBestStartingCellRow);
    }
    private int[] unfoldBestPathFromCell(int colNum, int rowNum)
    {
        PathInformation currentCellInformation = getInformationForBestPathFromCell(colNum, rowNum);
        int[] path = new int[currentCellInformation.length];
        path[0] = matrix[colNum][rowNum];
        int idx = 1;

        while(currentCellInformation.length > 1)
        {
            path[idx] = matrix[currentCellInformation.nextCellColumn][currentCellInformation.nextCellRow];
            idx++;
            currentCellInformation = getInformationForBestPathFromCell(currentCellInformation.nextCellColumn, currentCellInformation.nextCellRow);
        }

        return path;
    }

    private PathInformation getInformationForBestPathFromCell(int colNum, int rowNum)
    {
        if(informationForBestPathFromCellMemory[colNum][rowNum] == null)
        {
            informationForBestPathFromCellMemory[colNum][rowNum] = calculateInformationForBestPathFromCell(colNum, rowNum);
        }
        return informationForBestPathFromCellMemory[colNum][rowNum];
    }
    
    private PathInformation calculateInformationForBestPathFromCell(int colNum, int rowNum)
    {
        List<PathInformation> possiblePathsFromCell = new ArrayList<PathInformation>();
        if(colNum != 0 && matrix[colNum - 1][rowNum] < matrix[colNum][rowNum])
        {
            PathInformation p = getInformationForBestPathFromCell(colNum - 1, rowNum);
            possiblePathsFromCell.add(new PathInformation(p.length + 1, matrix[colNum][rowNum], p.endValue, colNum - 1, rowNum));
        }

        if(colNum != matrix.length - 1 && matrix[colNum + 1][rowNum] < matrix[colNum][rowNum])
        {
            PathInformation p = getInformationForBestPathFromCell(colNum + 1, rowNum);
            possiblePathsFromCell.add(new PathInformation(p.length + 1, matrix[colNum][rowNum], p.endValue, colNum + 1, rowNum));
        }

        if(rowNum != 0 && matrix[colNum][rowNum - 1] < matrix[colNum][rowNum])
        {
            PathInformation p = getInformationForBestPathFromCell(colNum, rowNum - 1);
            possiblePathsFromCell.add(new PathInformation(p.length + 1, matrix[colNum][rowNum], p.endValue, colNum, rowNum - 1));
        }

        if(rowNum != matrix[colNum].length -1 && matrix[colNum][rowNum + 1] < matrix[colNum][rowNum])
        {
            PathInformation p = getInformationForBestPathFromCell(colNum, rowNum + 1);
            possiblePathsFromCell.add(new PathInformation(p.length + 1, matrix[colNum][rowNum], p.endValue, colNum, rowNum + 1));
        }

        if(possiblePathsFromCell.isEmpty())
        {
            return new PathInformation(1, matrix[colNum][rowNum], matrix[colNum][rowNum], -1, -1);   
        }

        return Collections.max(possiblePathsFromCell);
    }
}

