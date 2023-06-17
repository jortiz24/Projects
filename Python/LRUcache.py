class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.cache = {}

        

    def get(self, key: int) -> int:

        if key in self.cache:
            val = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = val 
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        else:
            self.cache[key] = value
            if len(self.cache) > self.capacity:
                for x in self.cache:
                    self.cache.pop(x)
                    break
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
