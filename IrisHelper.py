from LGP import LGP

import numpy as np
import matplotlib.pyplot as plt
# --------- FORMAT DATA -------------

# Read data as [float, float, float, float, dict]
data = np.genfromtxt("Data/iris/iris.data", delimiter=",", dtype=(float, float, float, float, dict))

# Values to map the classes to int
classes = {
    b'Iris-setosa':0,
    b'Iris-versicolor':1,
    b'Iris-virginica':2
}

# Do python conversion 'cause i don't know any better 🤪
data_array = []
for i in range(len(data)):
    dta = []
    for j in range(4):
        dta.append(data[i][j])
    dta.append(classes[data[i][4]])
    data_array.append(dta)

# Convert to numpy
data_set = np.array(data_array)

# Shuffle array
np.random.shuffle(data_array)

# get the number of how many to train and how many to test
train = int(len(data_array)*80/100)
test = int(len(data_array)*20/100)

# ----------- GENETIC PROGRAM ----------------
lgp = LGP(4, 3, 10, data_set[0:train], data_set[train:], 80, 20, 1)
# 
# # Get scores    
# b = lgp.best_scores
# w = lgp.worst_scores
# 
# 
# x = np.arange(21)
# 
# plt.plot(x, b, color="green")
# plt.plot(x, w, color="red")
# 
# 
# plt.show()