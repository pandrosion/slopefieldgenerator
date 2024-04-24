''' 
Author: B. W. Black 
Created: 18 April 2024 
Last modified: 18 April 2024

This program will obtain an ordinary differential equation of order 2 or lower 
with the option of adding initial conditions and do the following:
    - Display the slope field, with the solution highlighted if initial conditions are given.
    - Identify any equilibrium, sink, saddle, or source points
    - If applicable, identify a characteristic equation and characteristic roots
    - If applicable, generate a general solution based on characterisic roots and, for non-homogenous ODEs, 
    generate a particular solution using variation of parameters.
'''

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import mpld3

# Generate some data
x = np.linspace(0, 10, 100)
y = 2 * x + 1

# Create the plot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Example Graph')

html_plot = mpld3.fig_to_html(fig)

with open('plot.html', 'w') as f:
    f.write(html_plot)

