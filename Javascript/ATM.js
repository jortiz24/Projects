''' Leetcode # 2241'''
var ATM = function() {
    

    bills = [0,0,0,0,0]

    dollars = [20,50,100,200,500]
};

/** 
 * @param {number[]} banknotesCount
 * @return {void}
 */
ATM.prototype.deposit = function(banknotesCount) {

    for(x = 0; x < banknotesCount.length; x++){
        
        bills[x] += banknotesCount[x];
        
        
    }
    
};

/** 
 * @param {number} amount
 * @return {number[]}
 */
ATM.prototype.withdraw = function(amount) {

    current = bills.slice()
    
    money = amount
    output = [0,0,0,0,0]
    for(x = 1; x < dollars.length +1 ; x++){
        
        
        total = Math.floor(money /dollars[dollars.length - x])
        

        if( total >= bills[dollars.length-x]){
            money = money - dollars[dollars.length-x]*bills[dollars.length-x];
            output[dollars.length-x] = bills[dollars.length-x]
            bills[dollars.length-x] = 0;
            

        }
        else{
            money = money - dollars[dollars.length-x]*total;
            output[dollars.length-x] = total
            bills[dollars.length-x] -= total;
        }
        

        if(money == 0){
            return output
        }

    }
    bills = current
    
    return [-1]
};

/** 
 * Your ATM object will be instantiated and called as such:
 * var obj = new ATM()
 * obj.deposit(banknotesCount)
 * var param_2 = obj.withdraw(amount)
 */
