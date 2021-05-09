#FlipPredictor
#A coin is drawn at random from a bag of coins of varying probabilities
#Each coin has the same chance of being drawn
#Your class FlipPredictor will be initialized with a list of the probability of 
#heads for each coin. This list of probabilities can be accessed as self.coins 
#in the functions you must write. The function update will be called after every 
#flip to enable you to update your estimate of the probability of each coin being 
#the selected coin. The function pheads may be called and any time and will 
#return your best estimate of the next flip landing on heads.


from __future__ import division
class FlipPredictor(object):
    def __init__(self,coins):
        self.coins=coins
        n=len(coins)
        self.probs=[1/n]*n
    def pheads(self):
        #Write a function that returns 
        #the probability of the next flip being heads 
        return sum(pcoin*p for pcoin,p in zip(self.coins,self.probs)) 

    def update(self,result):
        #Write a function the updates
        #the probabilities of flipping each coin
        
        pheads=self.pheads()
        if result=='H':
            self.probs=[pcoin*p/pheads for pcoin,p in zip(self.coins,self.probs)]
        else:
            self.probs=[(1-pcoin)*p/(1-pheads) for pcoin,p in zip(self.coins,self.probs)]
            
            
            
            
