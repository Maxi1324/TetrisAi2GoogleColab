# %%
import Prepare


# %%
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten

from rl.policy import BoltzmannQPolicy

# %%
trainstep = 1000000
learningrate = 1e-3
warmup = 100

rewardHoch = 4
rewardmult = 2
alwaysReward = 0.000000001

render = False

verbose = 3000

speed = 10

loadfile = None
savefile = "BoltzTiny"

# %%

model =  Sequential([
        Dense(1, activation='relu', input_shape=(1,20,10,1)),
        Flatten(),
        Dense(25, activation='relu'),
        Dense(25, activation='relu'),
        Dense(25, activation='relu'),
        Dense(5, activation='relu'),
    ])

print(model.summary())
    
policy = BoltzmannQPolicy() 

import ScriptBase;


