''' leetcode # 2353'''

/**
 * @param {string[]} foods
 * @param {string[]} cuisines
 * @param {number[]} ratings
 */
var FoodRatings = function(foods, cuisines, ratings) {


    rating = {}
    food = {}

    for(x = 0; x < foods.length; x++){

        rating[foods[x]] = ratings[x];

        if(food[cuisines[x]] == undefined ){
            
            food[cuisines[x]] = [foods[x]]
            
           
        }
        else{
             food[cuisines[x]].push(foods[x]);
        }
        
    }
   
  

    
};

/** 
 * @param {string} food 
 * @param {number} newRating
 * @return {void}
 */
FoodRatings.prototype.changeRating = function(food, newRating) {

    rating[food] = newRating
    
};

/** 
 * @param {string} cuisine
 * @return {string}
 */
FoodRatings.prototype.highestRated = function(cuisine) {
    
    let output = []
    meals = food[cuisine]

    for( x in meals){
        
        if(output.length == 0){
            output.push(meals[x])
           
            
            
        }else{

            if(rating[output[0]] === rating[meals[x]]){

                output.push(meals[x]);
               
            }

            if((rating[output[0]]) < (rating[meals[x]]) ){
              
                output = [meals[x]]
               
            }

           

        }
        
    }

    if(output.length > 1){

        highest = output[0]
        

        for(x in output){
            
            if(output[x] < highest){
                highest = output[x]
                
            }
        }
        return highest
    }
   
    return output[0]

    
};

/** 
 * Your FoodRatings object will be instantiated and called as such:
 * var obj = new FoodRatings(foods, cuisines, ratings)
 * obj.changeRating(food,newRating)
 * var param_2 = obj.highestRated(cuisine)
 */
