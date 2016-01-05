public class PathInformation implements Comparable<PathInformation>
{
    int length;
    int startValue;
    int endValue; 
    int nextCellColumn;
    int nextCellRow;

    public PathInformation(int length, int startValue, int endValue, int nextCellColumn, int nextCellRow) 
    {
        this.length = length;
        this.startValue = startValue;
        this.endValue = endValue;
        this.nextCellColumn = nextCellColumn;
        this.nextCellRow = nextCellRow;
    }

    @Override
    public int compareTo(PathInformation other) {
        if(this.length < other.length || (this.length == other.length && this.startValue - this.endValue < other.startValue - other.endValue)){
            return -1;
        }
        if(this.length > other.length || (this.length == other.length && this.startValue - this.endValue > other.startValue - other.endValue)){
            return 1;
        }
        return 0;
    }
}
