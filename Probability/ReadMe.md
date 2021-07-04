



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
    
    #find MLE or fit guassian  is nothing but finding finding standard deviation. 



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



# Binomial Distribution:

      binomial distribution is used when there large no of experiment of same you have to find probability of event same type

      for computing we use combination

      accumulative outcome of many coin flip

      for ex. fliping coin  n times what is probability of coming head k times  == p(head) = 0.8

      n!/(n-k)!*k!  *  p^k * (1-p)^(n-k)

      fliping coin 5 times what is p(h=3)

      5!/3!*2! * (0.8)^3 * (0.2)^2


# Central Limit Theoram:
    
    it is about sum of large or many experiment mostly n>=30
    then it is result is function jusk like gaussian graph
    
    we use formula n!/n-k! * k!
    
    example if coin is tossed many time what is outcome
            k=0    1    2     3    4
    n=1      1     1
    n=2      1     2    1 
    n=3      1     3    3     1
    n=4      1     4    6     4    1
    
    this pascal triangle
    if there is 3 outcom then we take addition of left 3 numbers
    

# Normal Distribution:
    
    it is aproximation of Bionomial Distribution it used to sum of many experiment.
    it normailized distribuition.
    
    its curve is bell curve area under it is not 1 but root of 2pisigm2
    
    normal distribution formula with mean mu and sigma2 
    
    
    f(x) =   1/ root of 2 *pi *sigma2   *   e raised to (-1/2 (x-mu)2/sigma2)
    
    
    for single coin flip or event we used simple probability.
    for few events or coin flips we used bionomial distributions
    
    for 10,000 or more coin flips we use normal distributions.
    
    
# Manipulating Normal Distribution:
    effect on mean and variance and standard deviation by adding contants
    if add x in elements then mean is increased by x and variance and standard deviation have no effect
    if multiply x in elemet then mean= mean*x and varaince sigma2 = x2*sigma@  and stand dev = square root of x*stand dev
    
    if you add 2 guassians then mean = 2*mean, variance = 2*variance
    
    
    A(mu, sigma2)   B(mu, sigma2)
    if A-B then mean=0, variance = 2*variance
    

# Confidence Interval (CI):
    
    confidence Interval is gives range where probability can lies. about 95% times probability lies between CI.
    as no of samples get increases CI range get's decreases and probability accuracy get increases.
    
    CI = 1.96 * Standard Deviation (sigma)/square root of N
    
    New Variance Formula
    sigma2 = p-p2
    
    New Std deviation Formula
    sigma = square root of (p-p2)
    
    New CI formula will be
    CI = 1.96 * square root of p(1-p)/N
    
# Normal Quantiles (NQ):
    
    magic number 1.96 which we used in CI is Normal Quantiles.
    95% confidence interal have 5% normal quantiles on both sides of gaussian graph in CLT.
    90% confidence interval have 10% of normal quantiles on both sides of guassian graph on CLT.
    
    CI = MEAN +- 1.96 * square root of sigma2/N
   
    95% CI = NQ = 1.96
    90% CI have NQ = 1.64
    99% CI have NQ = 2.58
  
  
 # Hypothesis Test:
 
    Hypothesis test is checking whether given hypothesis or information is correct or not.
    
    there are 2 hypothesis in example.
    Null Hypothesis -- it is correct hypothesis ex. cancer drug cure 80% of people so p(0.8) is null hypothesis.
    Alternate Hypothesis -- it is wrong hypothesis ex.  p < 0.8 is alternate hypothesis
    
    critical region :
        when testing hypothesis we check whether sample of events lies in critical region which is boundary of alternate
        hypothesis.
        
        it 5% of bionomial distribution . 0.05 we calculate at what no sample addition of probability is 0.05
        
        first calculate bionomial distribution for sample starting from 0 to till last sample. 
        then we sum binomial distribution of sample which is less than 0.05
        
        for cancer example. 
        1 2 3    4    5    6   7 and so on
        0 0 0.01 0.01 0.02
        at 5th hypothesis sums of 0.05 so if 5 patients get cancer out of 10 then hypothesis is failed.
    
    We can also test hypothesis using Confidence Interval.
    for ex. given hypothesis we can find out confidence interval which is as follows
      mean +- 1.96(for 5%) * sq root of sigma2/n 
      
      if claim is within this C.I range then it is true. else it is alternate hypothesis is true.
    
    
    
    
    
    
    
    
    
    
    
    


    
    
    


