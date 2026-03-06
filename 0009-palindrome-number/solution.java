class Solution {
    public boolean isPalindrome(int x) {
        int sum=0;
        int y=x;
        if(x<0)
        {
            return false;
        }
            while(x!=0)
            {
                int mod=x%10;
                sum=sum*10 +mod;
                x=x/10;
            }
            return y==sum;
    }
}
