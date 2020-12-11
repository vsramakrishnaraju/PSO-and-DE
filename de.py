from diffevo import de_simple
from diffevo.cost_functions import sphere

# https://github.com/nathanrooy/differential-evolution-optimization referance 

bounds = [(-10,10),(-10,10)]    

popsize = 10        

mutate = 0.5         

recombination = 0.7       

maxiter = 20            

de_simple.minimize(sphere, bounds, popsize, mutate, recombination, maxiter)
