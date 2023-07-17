#Leetcode # 258

# @param {Integer} num
# @return {Integer}
def add_digits(num)
    

    if num.div(10) == 0
        return num
    end
    output = 0

    copy = num

    while copy != 0


        output = output + copy % 10
        print(output)
        copy = copy.div(10)

        if copy == 0
            if output >= 10
                copy = output
                output = 0
            end
        end

    end

    return output
end
