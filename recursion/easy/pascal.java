class Solution{
    public static int numberOfDots(int x){
        if (x <= 1) return 1;
        return x + numberOfDots(x-1);
    }
}
