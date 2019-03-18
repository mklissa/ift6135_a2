import matplotlib.pyplot as plt
import numpy as np
import os
import pdb

# pdb.set_trace()
arch='TRANSFORMER'
path = "{}_losst.npy".format(arch)

losst = np.load(path)

fig,ax = plt.subplots(1)
ax.set_title("Comparison over architectures for loss over timesteps")
ax.plot(losst,label=arch)
ax.set_xlabel("Timestep")
ax.set_ylabel("Loss")
ax.legend()
ax.plot()
plt.savefig("plots/5.1/all_architectures.jpg")