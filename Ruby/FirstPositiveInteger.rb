### Leetcode#41

# @param {Integer[]} nums
# @return {Integer}
def first_missing_positive(nums)

    check = Array.new(nums.length,0) ###This is a little inefficient timewise but still works


    if nums.length == 1

        if nums[0] == 1
            return 2
        else
            return 1
        end

    end

    for x in nums

        if x > 0 and x <= nums.length
            if !(check.include?(x))
                check[x-1] = x
            end
        end


    end

    print(check)
    for x in (0..check.length)
    
        if check[x] == 0
            return x + 1
        end

    end

    return nums.length + 1
    
end
