###############################################
### CMPLXSYS425 - Evolution in silico       ###
### Lab 1                                   ###
### ####################################### ###
### IF YOU HAVEN'T LOOKED AT THE NOTEBOOKS  ###
### ON GITHUB FIRST, PLEASE DO THAT!        ###
###############################################

import numpy as np
from matplotlib import pyplot as plt

def mutation_function(org, mut_prob):
  new_org = org
  #We mutate! 
  if np.random.rand() < mut_prob:
    if(org == 0):
      new_org = 1
    else:
      new_org = 0
  return new_org
            

prob_mutation = 0.2
prob_repro = 0.50
num_replicates = 100
num_generations = 10 #let's run a little longer this time

populations = [[0] for rep_idx in range(num_replicates)]
pop_sizes = [[] for rep_idx in range(num_replicates)]

for rep in range(num_replicates): 
  this_population = populations[rep]

  for generation in range(num_generations):
    for pop_idx in range(len(this_population)):
      if np.random.rand() < prob_repro:
        org_to_add = mutation_function(this_population[pop_idx], mut_prob=prob_mutation)
        this_population.append(org_to_add)

    pop_sizes[rep].append(len(this_population))

proportion_mutants = [sum(rep_pop)/len(rep_pop) for rep_pop in populations]

plt.hist(proportion_mutants)
plt.title("Proportion Resistant")
plt.show()