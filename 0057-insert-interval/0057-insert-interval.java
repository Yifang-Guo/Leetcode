class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> merged = new ArrayList<>();
        for(int[] interval : intervals){
            if(newInterval == null || interval[1] < newInterval[0]){
                merged.add(interval);
            }else if(interval[0] > newInterval[1]){
                merged.add(newInterval);
                merged.add(interval);
                newInterval = null;
            }else{
                newInterval[0] = Math.min(interval[0], newInterval[0]);
                newInterval[1] = Math.max(interval[1], newInterval[1]);
            }
        }
        if(newInterval != null){
            merged.add(newInterval);
        }
        return merged.toArray(new int[merged.size()][]);
    }
}