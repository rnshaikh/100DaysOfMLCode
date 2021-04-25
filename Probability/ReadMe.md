



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



# probability Distributions:

In continous Distributions, every outcome has probability 0

ex. probability of spining pen in circle landing at 180 is 0


# Range probility Instead

ex. p(0<=x<=180) = 1/2 chances landing between 0-180 and 180-360


