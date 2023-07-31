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
            
            if(pref.length + suff.length <= letter[letter.length - x - 1].length ){
                
                
                
                if(word.substring(0,pref.length) === pref && word.substring(word.length - suff.length,word.length) === suff ){
                    
                    return letter.length - x - 1
                }
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
 * var param_1 = obj.f(pref,suff)
 */
