/** leetcode #745
 * @param {string[]} words
 This solution is different from Leetcode because I broke up the inputs into dictionary by first letter for better efficiency 
 However the solution only accepts returning index from a list that has all the inputs in one rather than organized in different lists*/
var WordFilter = function(words) {
    
    dictionary = {}

    for(x in words){

        if(words[x][0] in dictionary){
            console.log(dictionary[words[x][0]])
            dictionary[words[x][0]].push(words[x ])
            
            
        } else{
            dictionary[words[x][0]] = [words[x]]
        }
    }


};

/** 
 * @param {string} pref 
 * @param {string} suff
 * @return {number}
 */
WordFilter.prototype.f = function(pref, suff) {
    
    console.log(dictionary)
    if(pref[0] in dictionary){

        letter = dictionary[pref[0]]
        for(x in letter){


            word =letter[letter.length - x - 1]

            if(word.length == 1 && word === suff && word === pref){
                return letter.length - x - 1
            }
            
           
                
                
                
            if(word.substring(0,pref.length) === pref && word.substring(word.length - suff.length,word.length) === suff ){
                    
                 return letter.length - x - 1
             }
            
        }


    }else{
        return -1
    }
    return - 1
};

/** 
 * Your WordFilter object will be instantiated and called as such:
 * var obj = new WordFilter(words)

 /**
 * @param {string[]} words
 Solution for leetcode version, changes dictionary to [] instead of {} and adjusts rest of code accordingly, definitely more inefficient. Maybe reverse dictionary once on initialization then search left to right instead of right to left would be faster*/
var WordFilter = function(words) {
    
    dictionary = []

    for(x in words){

        
        dictionary.push(words[x ])
            
        /** if list is reversed output would have to be inversed as well, length - index to correspond to 'largest' index for leetcode solution*/
      
    }


};

/** 
 * @param {string} pref 
 * @param {string} suff
 * @return {number}
 */
WordFilter.prototype.f = function(pref, suff) {
    
    
    


    for(x in dictionary){

        
        word =dictionary[dictionary.length - x - 1]
        //console.log(word.substring(word.length - suff.length,word.length),pref,suff)

        if(word.length == 1 && word === suff && word === pref){
            return dictionary.length - x - 1
        }
            
        
                
                
                
        if(word.substring(0,pref.length) === pref && word.substring(word.length - suff.length,word.length) === suff ){
                    
                return dictionary.length - x - 1
            }
            
        }


    return - 1
    };

/** 
 * Your WordFilter object will be instantiated and called as such:
 * var obj = new WordFilter(words)
 * var param_1 = obj.f(pref,suff)
 */
 * var param_1 = obj.f(pref,suff)
 */
