[![Open Class Repo on Repl.it](https://repl.it/badge/github/unknownblueguy6/MineSweeper)](https://repl.it/github/zamanlh/EvolutionInSilico_Current)

# Lab1 - Luria-Delbrück Simulation
The first lab for Evolution in Silico! 

## Overview
Recall from our lectures (or re-watch if you need a bit of a refresher) that the Luria-Delbrück experiment -- sometimes called a fluctuation test -- was a way to determine if mutations are random, or if they occur **because of** (i.e., in response to) the environment. 

Now that we know that mutations **are** random, you might think the Luria-Delbrück protocol is no longer relevant. But, people also use this exact same protocol to measure the *mutation rate* of a particular trait, like antibiotic resistance. 

In this lab we'll implement a Luria-Delbrück simulation, and use it to gain an intuition for the stochastic nature of mutations, how the original experimental design is able to distinguish between *random* mutations and *directed* mutations, and see how mutation rates could be measured. 

## Intro Code
There are two Jupyter Notebooks in this lab repository, `Intro_1.ipynb` and `Intro_2.ipynb`. Once you've got the assignment over on GitHub, you'll be able to click on these and view them right in your web browser -- no launching python necessary!

You should look through these, especially if you haven't programed in Python in a while or haven't made many simulations. Don't worry if everything doesn't make sense yet, I'm throwing you all in the deep end a bit here. Some of you will blow through this quickly, and that's great! I hope there is plenty of interesting bits to play with, even if all the code and simulations already make sense to you. 

## Repl.it
Once you've looked through the Jupyter Notebooks, you should also see a button to launch the Repl.it IDE. This will launch a little virtual environment where you can edit code and run it in your browser! It's a full virtual machine that gets launched when you click that button, which I think is pretty neat. It even has a ***multiplayer*** mode, where you all will be able to work on group assignments together. 

We'll play with this together during the synchronous lab session, but if you couldn't make it and have any questions or issues feel free to reach out! 

## What you should do
In `lab.py`, I copied the result of the first two Jupyter notebooks into a normal Python script. When you hit **Run**, you should see the code run and the figure pop-up. It might take a second the first time, and it might not look right. For me, it looked fine after the second or third time I ran it. It's an impressive tool, so I'm okay forgiving a few of these annoying bugs. 

### Play with the parameters
- Change the probability of reproduction and notice how the histogram changes
- Change the number of generations (though remember this is exponential growth so don't go *too* big)
- Change the mutation rate and notice what happens to the distribution (helps if it is small, and the number of generations is a bit larger)

### Change the simulation to model **directed** mutations
As we built this simulation up, we were assuming mutations occurred randomly during growth. But, the alternative explanation for the Luria-Delbrück experiment was that mutations were triggered by exposure to the stressful condition. Modify our simulation to see what the distribution of mutants would look like if mutations were *directed* rather than *random*. 
 - During growth, mutations no longer occur
 - After growth, every organism in the population is exposed to some stress and with some probability (`prob_directed_mut` could be a name for this), the organism mutates into the alternative genotype (becomes `1`).

### Think about the differences between the distributions of resistant mutations in these two alternative situations
- Do they depend on the number of generations?
- Does it seem like you could easily distinguish these two hypotheses?
- How many replicate populations do you need to tell them apart? 
- You could even try making movies of the distributions changing as something like mutation rate or generations increases! 



