class Solution {
    public int romanToInt(String s) {
        int pre=0;
        int curr;
        int total=0;
        for (int i=s.length()-1;i>=0;i--)
        {
            curr=switch(s.charAt(i))
            {
                case 'I'-> 1;
                case 'V'-> 5;
                case 'X'-> 10;
                case 'L'-> 50;
                case 'C'-> 100;
                case 'D'-> 500;
                case 'M'-> 1000;
                default ->0;
            };
            if (curr<pre)
            {
                total-=curr;
            }
            else
            {
                total+=curr;
            }
            pre=curr;
        }
        return total;
    }
}
