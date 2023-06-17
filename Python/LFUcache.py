class LFUCache:
    
    def __init__(self, capacity: int):

        self.capacity = capacity
        self.cache = {}
        

        

    def get(self, key: int) -> int:

        if key in self.cache:
            val = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = [val[0],val[1] + 1]
            

             
            return self.cache[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            counter = self.cache[key][1]
            self.cache.pop(key)
            self.cache[key] = [value,counter + 1]
        else:
            
            if len(self.cache) == self.capacity:
                
                minimum = min([x[1] for x in list(self.cache.values())]) #### This line right here isn't efficient, O(n) instead of O(1) 
                ### importing numpy or something else to slice columns might be more efficient not sure
                
               
                for x in self.cache:
                    
                    
                    
                    if  self.cache[x][1] == minimum:
                        self.cache.pop(x)
                        self.cache[key] = [value,1]
                        break
    

                    

            else:
                self.cache[key] = [value,1]
                        
                    


                
        
        

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
