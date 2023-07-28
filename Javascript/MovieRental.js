'''Leetcode # 1912'''
class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):

        self.shops = {}  ''' {shop:[list of movies}
        self.prices = {} ''' {price:{movie: [list of shops with movie at this price]}}
        self.rented = [] ''' [[shop,movie]] 

        

        for x in entries:
            
            

            if x[0] in self.shops:

                self.shops[x[0]] += [x[1]]

            else:
                self.shops[x[0]] = [x[1]]


            
            if x[2] in self.prices:

                if x[1] in self.prices[x[2]]:
                
                    self.prices[x[2]][x[1]] += [x[0]]  
                else:
                    self.prices[x[2]][x[1]] = [x[0]]
            else:
               # print(x[0],x[1],x[2])
                self.prices[x[2]] = {x[1]:[x[0]]}
            

            


        sort = sorted(self.prices.items())
        
        self.prices = {}
        for key,value in sort:
            self.prices[key] = value
        
        
        
     
            
            

    def search(self, movie: int) -> List[int]:

        output = []

        for x in self.prices:

            if movie in self.prices[x]:
                shops = []
                
                for y in self.prices[x][movie]:
                    
                   # print(self.shops)
                    #print()
                    #print(self.prices)

                    if movie in self.shops[y]:
                        shops += [y]

                output += sorted(shops)
                
                if len(output) >= 5:
                    return output[:5]

        


        return output

    def rent(self, shop: int, movie: int) -> None:

        self.rented += [[shop,movie]]

        self.shops[shop].remove(movie)

        

    def drop(self, shop: int, movie: int) -> None:
        
        self.rented.remove([shop,movie])

        self.shops[shop] += [movie]
        

    def report(self) -> List[List[int]]: ''' this part is a little messy but keeps it sorted at least

        output = []

        for x in self.prices:
            movieorder = sorted(self.prices[x].keys())
            
            for y in movieorder:
                    #### for y in rented[:][]
                for z in self.prices[x][y]:
                    if [z,y] in self.rented:
                        output += [[z,y]]
                
                        if len(output) == 5:
                            return output
        return output







        


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
