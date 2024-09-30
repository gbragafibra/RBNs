import numpy as np

def AND(inputs):
    return 1 if np.all(inputs == 1) else 0

def OR(inputs):
    return 1 if np.any(inputs == 1) else 0

def NAND(inputs):
    return 1 - AND(inputs)

def NOR(inputs):
    return 1 - OR(inputs) 

def XOR(inputs):
    return 1 if np.sum(inputs) % 2 != 0 else 0

def XNOR(inputs):
    return 1 - XOR(inputs) 

def Tautology(inputs):
    return 1 #return 1 regardless of inputs

def Contradiction(inputs):
    return 0 #return 0 regardless of inputs