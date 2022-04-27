# Plot Z plane

Python library for plotting complex functions transformations

## It can...

- *plot complex planes (both transformed and original)*
- *plot transformations of specific areas (both transformed and original)*
- *plot lines parallel to real or imaginary axes (both transformed and original)*

## Usage

### plotcp_plt

To plot f(z) = (z+1)/z with x bound from -4 to 4 and y bound from -4 to 4

```python3
from plotly_z import plot_z


def f(z: complex) -> complex:  # Define function to plot
    return (z + 1) / z


# Call plot_z
# Second and third arguments define limits of a plot
fig = plot_z(f, (-4, 4), (-4, 4))
```

For full parameters list check ```help(plotly_z.plot_z)```

### plot_complex_points

```python3
import numpy as np
from plotly_z import plot_complex_points


def f(z: complex) -> complex:  # Define function to plot
    return np.sin(z)


# Define area to be plotted
top = [x + 2 * 1j for x in np.linspace(1, 2, 5)]
bottom = [x + 1 * 1j for x in np.linspace(1, 2, 5)]
left = [1 + y * 1j for y in np.linspace(1, 2, 5)]
right = [2 + y * 1j for y in np.linspace(1, 2, 5)]

# Plot original area
fig = plot_complex_points(top, name='top initial', color='red')
fig = plot_complex_points(bottom, fig=fig, name='bottom initial')
fig = plot_complex_points(left, fig=fig, name='left initial')
fig = plot_complex_points(right, fig=fig, name='right initial')

# Apply function to area and plot it on a new plot
fig2 = plot_complex_points([f(z) for z in top], name='top transformed', color='red')
fig2 = plot_complex_points([f(z) for z in bottom], fig=fig2, name='bottom transformed')
fig2 = plot_complex_points([f(z) for z in left], fig=fig2, name='left transformed')
fig2 = plot_complex_points([f(z) for z in right], fig=fig2, name='right transformed')

fig.show()
fig2.show()
```

For full parameters list check ```help(plotly_z.plot_complex_points)```

# Matplotlib version

Matplotlib (old) version you can find [here](https://github.com/ZettZet/plotcp)