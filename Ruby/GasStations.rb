# Leetcode # 134
# @param {Integer[]} gas
# @param {Integer[]} cost
# @return {Integer}
def can_complete_circuit(gas, cost)
    skip = 0
    counter = 0

    (0..gas.length-1).each do |x|

        if skip > x
            x = skip
        end

        
        
      
        cgas = 0
        ccost = 0
          
        while true  
            if counter > gas.length 
                return x
            end

            position = (x+counter)%gas.length

            cgas += gas[position]
            ccost += cost[position]

            if ccost > cgas
                skip = x
                counter = 0
                break
            end
            
            counter += 1
        end
    end
    return -1
end
