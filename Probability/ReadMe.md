



# Baye's Theorm :

    Prior probability  . test evidence = posterior probability

    problem

    1% of population have cancer.
    90% chances that if you have cancer test is positive.
    90% chances that if you dont have cancer test is negation

    this dependent probability

    prior probability:
        P(c) = 0.01  P(>c) = 0.99

    Sensitivity:
        P(tp| c) = 0.9  P(tn | c) = 0.1

    Specitivity:
    P(tn | >c) = 0.9  P(tp | >c) = 0.1


    find out P(tp)
    P(c | tp) , P(>c | tp)

    P(c|tp) = P(c) * P(tp|C) = 0.01 * 0.9 = 0.009
    P(>c|tp) = P(>c) * P(tp|>c) = 0.99 * 0.1 = 0.099


    P(tp) = P(c|tp) + P(>c|tp) = 0.108

    so addtion of P(c|tp), P(>c|tp) does not comes 1 so we have to normalize
    it by dividing by P(tp) = 0.108

    Normalizing:

    Posterior Probabiltiy:
    P(c|tp) = P(c|tp) % P(tp) =  0.0833
    P(>c|tp) = P(>c|tp) % P(tp) = 0.9167    now this is equal to 1




    P(home| rain) = P(home) * P(rain|home)  = 0.4 * 0.01 = 0.004

    P(gone|rain)  = P(gone) * P(rain|gone) = 0.6* 0.3 = 0.18

    P(rain)  = P(home| rain) + P(gone | rain) =  0.184



    P(H) = P(c1 | H) + P(c2 | H)

    P(c1| H) = P(C1)* P(H|C1) = 0.15

    p(c2| H) = P(c2) * P(H|C2) = 0.63



    p(c|neg)  = p(c) * p(tn|c)

    p(>c}neg) = p(>c) * p(tn|>c)
    p(neg) = p(c/neg) + p(>c|neg)



# Probability Distributions:

    In continous Distributions, every outcome has probability 0

    ex. probability of spining pen in circle landing at 180 is 0


# Range probility Instead

    ex. p(0<=x<=180) = 1/2 chances landing between 0-180 and 180-360

    ex. p(260 <= x <= 290) = 1/12 chances landing between 260-290 and 290-320 so on.

    ex. p(0 <= x <= 1) = 1/360 chances landing in 1 degree range

    p(a<= x <= b) = size(b-a)/360



# Density:

    f(x) == probability of continous distribution.

    constraints: 1) each outcome has equal value.
                 2) area under density is equal or greater than 1
                 3) alwayse positive

    density of point in 0-360

    f(x) = 1/360 = 0.00277


    ex.2) date and time you were born
    x= seconds

    p(x) =  0  as it is continous distributions
    f(x) =  1/60 = 0.01666



    ex.3) people born before noon twice as likely as people born after noon
    x= hours

    f(x before noon) = 2(x after noon)

      b  |_____
      a  |_____|____
         |_________x_____

     3 part of density

     a = 1/3 * 1/12 = 0.02777777777

     b = 2*a = 0.055555


     ex.4) density between 3 to 3/12 min

     x=min

    f(x) = 1/(1/2) = 2
 
# Corelation and Causation:

    correlation :  if x some of property tells something about other property y in data plot on graph.

    causation :  tells about what is cause of x being happend.


    ex.   sick     in-hospital -- 4 died out 100
                   in-home ----> 20 died out 100

          here variable in-hospital is correlate with dead
          and cause is sick which cause to hospitalized but it is ignore in statistics


# Estimation
    
    there are two types of estimation.
    MLE = minimum likelihood estimator
    LPC = Laplacian estimator
    
    MLE = possible outcome / total no of out come
     
    if there is not much data then we add fake data for every possible outcome
    then MLE become Laplace estimator
    
    ex. 1) 1011 : 1-head 0-tail
    MLE?  MLE = 3/4 = 0.8
    
    ex. 2) 0 
        MLE = 0
    in this case add fake data
        010     
        LPC = 1/2 = 0.5
   
        
        
        
    
    
    
    
    
    
    


ex. p(260 <= x <= 290) = 1/12 chances landing between 260-290 and 290-320 so on.


ex. p(0 <= x <= 1) = 1/360 chances landing in 1 degree range


p(a<= x <= b) = size(b-a)/360



# Density:

    f(x) == probability of continous distribution.

    constraints: 1) each outcome has equal value.
                 2) area under density is equal or greater than 1
                 3) alwayse positive

    density of point in 0-360

    f(x) = 1/360 = 0.00277


    ex.2) date and time you were born
    x= seconds

    p(x) =  0  as it is continous distributions
    f(x) =  1/60 = 0.01666



    ex.3) people born before noon twice as likely as people born after noon
    x= hours

    f(x before noon) = 2(x after noon)

  b  |_____
  a  |_____|____
     |_________x_____

     3 part of density

     a = 1/3 * 1/12 = 0.02777777777

     b = 2*a = 0.055555


     ex.4) density between 3 to 3/12 min

     x=min

    f(x) = 1/(1/2) = 2





# Corelation and Causation:

correlation :  if x some of property tells something about other property y in data plot on graph.

causation :  tells about what is cause of x being happend.


ex.   sick     in-hospital -- 4 died out 100
               in-home ----> 20 died out 100

      here variable in-hospital is correlate with dead
      and cause is sick which cause to hospitalized but it is ignore in statistics





p(coin | flip)  = p(coin) * p(flip | coin) / p(flip)

p(h)  = sum(p(coin)*p(h))

p(coin | h)  = p(coin) * p(h) / p(h)

p(coin | t) = p(1-coin) * p(h) / p(1-h)










