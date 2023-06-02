"Leetcode #260"
  class Solution {
    public int[] singleNumber(int[] nums) {

        int[] output;
        ArrayList<Integer> exists;
        exists = new ArrayList<Integer>();
        

        
        

        for(int x = 0; x < exists.size(); x++){
            if(exists.contains(nums[x]))
            {
                exists.remove(x);
            } 
            else
            {
                exists.add(x);
            }


        }
        System.out.println(exists);
        
        output = exists.toArray( );
        
        return output;
    }
}
