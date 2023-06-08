# Leetcode # 134
# @param {Integer[]} gas
# @param {Integer[]} cost
# @return {Integer}
def can_complete_circuit(gas, cost)
    
    if gas.sum < cost.sum
        return -1
    end

    start = 0
    position = 0
    cgas = 0
    ccost = 0



    while position < gas.length do

        

       
        
      
        cgas  += gas[position]
        ccost += cost[position]

        if position == start and cgas < ccost
            while position == start and gas[position] < cost[position] do
                position += 1
                start = position
            end
            
            cgas = 0
            ccost = 0
        
        elsif position != start and cgas < ccost then

            cgas = 0
            ccost = 0
            start = position
        
        else
            position += 1
        
        end
          
        
    end

    return start
end
