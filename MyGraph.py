import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 200)
plt.plot(x, np.sin(x))
plt.show()


## Creating a new virtual environment
## CODE: py -3 -m venv .venv
## Input above code directly in terminal 
## .venv is the name of the environment

## This activated the new virtual environment
## CODE: .\.venv\Scripts\activate

## Installs matplotlib
## CODE: pip install matplotlib