class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int[] currentMinCost = new int[cost.length+1];
        int i;

        for (i = 0; i < cost.length; i++) {
            currentMinCost[i+1] = Math.min(cost[i]+currentMinCost[i], currentMinCost[i+1]);
        if (i < cost.length-1) currentMinCost[i+2] = cost[i]+currentMinCost[i]; // if we're not on the last step
        }

        return currentMinCost[currentMinCost.length-1];
    }
}
