# Leetcode # 134
# @param {Integer[]} gas
# @param {Integer[]} cost
# @return {Integer}
def can_complete_circuit(gas, cost)

  


    (0..gas.length).each do |x|
        counter = x
        cgas = 0
        ccost = 0
        (0..gas.length).each do |y|
            
            cgas = cgas + gas[counter%gas.length]

            break if cgas < ccost + cost[counter%gas.length]

            ccost += cost[counter%gas.length]

            
            counter += 1

           

            if  counter % gas.length == x
                return x
            end
        end
    end

    return -1
end
