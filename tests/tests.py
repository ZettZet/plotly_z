import numpy as np

from plotly_z import plot_z, plot_complex_points, Reim


def f(z):
    return np.sin(z)


top = [x + 2 * 1j for x in np.linspace(1, 2, 5)]
bottom = [x + 1 * 1j for x in np.linspace(1, 2, 5)]
left = [1 + y * 1j for y in np.linspace(1, 2, 5)]
right = [2 + y * 1j for y in np.linspace(1, 2, 5)]

fig = plot_z(f, (-4, 4), (-4, 4), reim=Reim.IM)
fig = plot_complex_points(top, name='top', color='red', fig=fig)
fig = plot_complex_points(bottom, name='bottom', fig=fig)
fig = plot_complex_points(left, name='left', fig=fig)
fig = plot_complex_points(right, name='right', fig=fig)

fig = plot_complex_points([f(z) for z in top], name='top_t', color='red', fig=fig)
fig = plot_complex_points([f(z) for z in bottom], name='bottom_t', fig=fig)
fig = plot_complex_points([f(z) for z in left], name='left_t', fig=fig)
fig = plot_complex_points([f(z) for z in right], name='right_t', fig=fig)

fig.show()
