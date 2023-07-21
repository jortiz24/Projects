###

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        

        print((queryIP.split(".")))
        print(len(queryIP.split(".")))

        if len(queryIP.split(".")) == 4:
            ip = queryIP.split(".")

            print(len(ip))
            
            for x in ip:

                if len(x) > 3:
                    return "Neither"

                if len(x) > 1 and x[0] == "0":
                    return "Neither"

                
                
                if x < "0" or  x > "255":
                    return "Neither"
            
            return "IPv4"
        
        if len(queryIP.split(":")) == 8:
            ip = queryIP.split(":")
            print(ip)
            ascii2 = [chr(x) for x in range(48, 58)] + [chr(x) for x in range(65,71)] + [chr(x) for x in range(97,103)]
            print(ascii2)

            for x in ip:
                
                print(len(x))
                if len(x) < 1 or len(x) > 4:
                    return "Neither"

                

                print(not all(x in ascii2 for x in ip))
                if not all(y in ascii2 for y in x):
                    return "Neither"

            
            return "IPv6"
                
            
        return "Neither"
