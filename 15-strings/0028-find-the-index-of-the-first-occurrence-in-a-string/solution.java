class Solution {
    public int strStr(String haystack, String needle) {
         if (needle.isEmpty())
        {
            return 0;
        }
        int nh=haystack.length();
        int nn=needle.length();
        for (int i=0;i<=nh-nn;i++)
        {
            if (haystack.substring(i,i+nn).equals(needle))
                return i;
        }
        return -1;
    }
}
