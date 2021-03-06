import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # There are never fewer than 10 rabbits, abort simulation when seen
    if CURRENTRABBITPOP < 10:
        pass
    
    # Probability of Rabbit Reproducing
    pRabRep = 1 - (CURRENTRABBITPOP / MAXRABBITPOP)
    
    for i in range(CURRENTRABBITPOP):
        if random.random() < pRabRep:
            CURRENTRABBITPOP += 1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # Abort simulation if Fox population less than 10
    if CURRENTFOXPOP < 10:
        pass
    
    # Probability of Eatting rabbit
    pEatRab = CURRENTRABBITPOP / MAXRABBITPOP
    
    for i in range(CURRENTFOXPOP):
        if random.random() < pEatRab:
            # If rabbit population lesser than 10 after eating, then don't eat
            if CURRENTRABBITPOP - 1 > 10:
                CURRENTRABBITPOP -= 1
                
                # 1/3 chance of reproducing when successfully hunted down rabbit
                if random.random() < 1/3:
                    CURRENTFOXPOP += 1
                    
        else:
            # 10 Percent chance of dying if failure
            if random.random() < 0.9:
                if CURRENTFOXPOP - 1 > 10:
                  CURRENTFOXPOP -= 1
    
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    rabbit_populations = []
    fox_populations = []
    
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    
    x = range(numSteps)
    
    pylab.plot(x, rabbit_populations)
    pylab.title("Rabbit Population VS Time")
    
    pylab.plot(x, fox_populations)
    pylab.title("Fox Population VS Time")
    
    coeff = pylab.polyfit(range(len(rabbit_populations)), rabbit_populations, 2)
    pylab.plot(pylab.polyval(coeff, range(len(rabbit_populations))))
    pylab.title("PolyFit 2nd Degree for Rabbit Population")
    
    coeff = pylab.polyfit(range(len(fox_populations)), fox_populations, 2)
    pylab.plot(pylab.polyval(coeff, range(len(fox_populations))))
    pylab.title("PolyFit 2nd Degree for Fox Population") 
    
    return (rabbit_populations, fox_populations)

runSimulation(200)    

