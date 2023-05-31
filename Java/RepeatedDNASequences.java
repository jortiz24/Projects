"Returns repeated DNA sequences of length 10 in String s"  

class Solution {
    public List<String> findRepeatedDnaSequences(String s) {

        List<String> output = new ArrayList<String>();

        if(s.length() < 11)
        {
            return output ;
        }
        List<String> compare = new ArrayList<String>();
      
        for(int x = 0;x < s.length() - 9; x++){
          
            
            String seq = (s.substring(x,x+10));

            if( compare.contains(seq))
                {
                    if(output.contains(seq) == false)
                    {
                         output.add(seq)  ;
                    }
                   
                  
                } 
            else
                {
                    compare.add(seq);
                }

        

        }

        return output; 
    }
}
