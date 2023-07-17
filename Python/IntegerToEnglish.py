###Leetcode #273

class Solution:
    def numberToWords(self, num: int) -> str:

        if num == 0:
            return "Zero"

        unique = {0:"",1:"One ",2:"Two ",3:"Three ",4:"Four ",5:"Five ",6:"Six ",7:"Seven ",8:"Eight ",9:"Nine ",10:"Ten ",11:"Eleven ",12:"Twelve ",13:"Thirteen ",14:"Fourteen ",15:"Fifteen ",16:"Sixteen ",17:"Seventeen ",18:"Eighteen ",19:"Nineteen ",20:"Twenty ", 30:"Thirty ",40:"Forty ",50:"Fifty ",60:"Sixty ",70:"Seventy ", 80: "Eighty ", 90: "Ninety "}


        digits = []
        output = ""
        copy = num

        while copy != 0:

            digits = [copy%10] + digits
            copy = copy // 10

        
        print(digits)


        while digits:


            if digits[0] == 0:
                digits.pop(0)

            elif len(digits)%3 == 0:
                output = output + unique[digits.pop(0)] + "Hundred "

                next = digits.pop(0)
                print(next)
                if next == 1:
                     single = digits.pop(0)
                     output = output + unique[10 + single]

                if next == 2:
                    output = output + unique[20] + unique[digits.pop(0)]
                if next == 3:
                    output = output + unique[30] + unique[digits.pop(0)]
                if next == 4:
                    output = output + unique[40] + unique[digits.pop(0)]
                if next == 5:
                    output = output + unique[50] + unique[digits.pop(0)]
                if next == 6:
                    output = output + unique[60] + unique[digits.pop(0)]
                if next == 7: 
                    output = output + unique[70] + unique[digits.pop(0)]
                if next == 8:
                    output = output + unique[80] + unique[digits.pop(0)] 
                if next == 9:    
                    output = output + unique[90] + unique[digits.pop(0)]
                if next == 0:
                    next = digits.pop(0)
                    print(next)
                    if next != 0:
                        output = output + unique[next]
                    

                if len(digits) + 1 > 9:
                    output = output + "Billion "

                elif len(digits) + 1 > 6:
                    output = output + "Million "

                elif len(digits) + 1 > 3:
                    output = output + "Thousand "
        
            elif len(digits)%3 == 2:
                next = digits.pop(0)
                if next == 1:
                     single = digits.pop(0)
                     output = output + unique[10 + single]



                if next == 2:
                    output = output + unique[20] + unique[digits.pop(0)]
                if next == 3:
                    output = output + unique[30] + unique[digits.pop(0)]
                if next == 4:
                    output = output + unique[40] + unique[digits.pop(0)]
                if next == 5:
                    output = output + unique[50] + unique[digits.pop(0)]
                if next == 6:
                    output = output + unique[60] + unique[digits.pop(0)]
                if next == 7:
                    output = output + unique[70] + unique[digits.pop(0)]
                if next == 8:
                    output = output + unique[80] + unique[digits.pop(0)]
                if next == 9:    
                    output = output + unique[90] + unique[digits.pop(0)]
                
                if len(digits) + 1 > 9:
                    output = output +  "Billion "

                elif len(digits) + 1 > 6:
                    output = output + "Million "

                elif len(digits) + 1 > 3:
                    output = output + "Thousand "
                
                
                

                

            
            else:
                output = output + unique[digits.pop(0)]

                if len(digits) + 1 > 9:
                    output = output +  "Billion "

                elif len(digits) + 1 > 6:
                    output = output + "Million "

                elif len(digits) + 1 > 3:
                    output = output + "Thousand "



        return output[0:len(output)-1]
