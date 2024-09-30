from gates import *
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

gates = [AND, OR, NAND, NOR, XOR, XNOR, Tautology, Contradiction]

N = 100
K = 10
W = np.random.choice((0,1), size = (N, N))
iter_ = 100 #number of iterations


#Assigning interactions and gate choice
idxs = [np.random.choice(N, (K, 2)) for _ in range(N)] #Interactions
gate_choice = np.random.choice(gates, (N, N)) # Choice gate for each node

#choosing number of noisy points
η = 1 #noise frac
noised_points = int(η * (N**2))

fig, ax1 = plt.subplots()
img1 = ax1.imshow(W, cmap="gray", vmin=0, vmax=1) 
ax1.set_title(f"K = {K}; η = {η}")
ax1.axis("off")

def update(*args):
    global W

    #Adding noise
    noise_idxs = np.random.choice(N, (noised_points, 2))
    W[noise_idxs] = 1 - W[noise_idxs] # flip bits
    
    for i in range(N):
        for j in range(N):        
            inputs = np.array([W[row, col] for row, col in idxs[i]])  
            W[i, j] = gate_choice[i, j](inputs)

    img1.set_array(W) 
    return img1,

print("Updating...")
    
Writer = animation.writers["ffmpeg"]
writer = Writer(fps=10, metadata=dict(artist="Me"), bitrate=1800)


ani = animation.FuncAnimation(fig, update, frames=iter_, interval=100, blit=True)
ani.save("rbn_animations/RBN_K10_n1.mp4", writer=writer)
plt.show()
print("Finished!")
