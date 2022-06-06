from typing import Callable, Optional, Iterator

import plotly.graph_objs as go
import numpy as np
from numpy.typing import ArrayLike

from plotly_z.enums import Reim


def plot_z(
        fun: Callable[[ArrayLike], ArrayLike],
        x_bound: tuple[int, int, int],
        y_bound: tuple[int, int, int],
        *,
        n_steps: int = 100,
        reim: Reim = Reim.BOTH,
        fig: Optional[go.Figure] = None
) -> go.Figure:
    """
    :param fun: your predefined function f(z)
    :param x_bound: real plot bounds
    :param y_bound: imaginary plot bounds
    :param n_steps: how many nodes will be on each line
    :param reim: which part to display: 'real', 'imag' or 'both' (named constants, correspondingly: Reim.RE, Reim.IM,
    Reim.BOTH) (only works with grid lines, and not areas)
    Inits.TRANSFORM, Inits.BOTH)
    :param fig: Figure object to plot on
    :return: plotly Figure object
    """
    if fig is None:
        fig = go.Figure()

    axes_config = {
        'showgrid': True,
        'gridwidth': 1,
        'zeroline': True,
        'zerolinewidth': 2,
    }

    fig.update_xaxes(**(axes_config | {'range': x_bound[:2], 'gridcolor': 'orange', 'zerolinecolor': 'orange'}))
    fig.update_yaxes(**(axes_config | {'range': y_bound[:2], 'gridcolor': 'blue', 'zerolinecolor': 'blue'}))

    match reim:
        case Reim.IM:
            fig = __add_imag(fig, fun, x_bound, y_bound, n_steps)
        case Reim.RE:
            fig = __add_real(fig, fun, x_bound, y_bound, n_steps)
        case Reim.BOTH:
            fig = __add_imag(fig, fun, x_bound, y_bound, n_steps)
            fig = __add_real(fig, fun, x_bound, y_bound, n_steps)

    return fig


def __add_imag(fig: go.Figure, fun: Callable[[ArrayLike], ArrayLike], x_bound: tuple[int, int, int],
               y_bound: tuple[int, int, int], n_steps: int) -> go.Figure:
    x_l, x_r, x_s = x_bound
    y_l, y_r, _ = y_bound
    real_fixed = np.arange(x_l, x_r + 1, x_s)
    imag = np.linspace(y_l, y_r, n_steps)
    parallel_to_imag = np.array([re + 1j * imag for re in real_fixed])

    for line in parallel_to_imag:
        f_parallel_imag = fun(line)
        fig.add_trace(
            go.Scatter(x=np.real(f_parallel_imag), y=np.imag(f_parallel_imag), name=f'{np.real(line[0])}',
                       line={'color': 'orange'}))

    return fig


def __add_real(fig: go.Figure, fun: Callable[[ArrayLike], ArrayLike], x_bound: tuple[int, int, int],
               y_bound: tuple[int, int, int], n_steps: int) -> go.Figure:
    x_l, x_r, _ = x_bound
    y_l, y_r, y_s = y_bound
    imag_fixed = np.arange(y_l, y_r + 1, y_s)
    real = np.linspace(x_l, x_r, n_steps)
    parallel_to_real = np.array([real + 1j * im for im in imag_fixed])

    for line in parallel_to_real:
        f_parallel_real = fun(line)

        fig.add_trace(
            go.Scatter(x=np.real(f_parallel_real), y=np.imag(f_parallel_real), name=f'{1j * np.imag(line[0])}',
                       line={'color': 'blue'}))

    return fig


def plot_complex_points(init_points: Iterator[complex], *,
                        fig: Optional[go.Figure] = None, **kwargs) -> go.Figure:
    """
    Plot complex points
    :param color:
    :param name: name of a line
    :param init_points: values to be plotted
    :param fig: Figure object to plot on
    :return: plotly Figure object
    """
    if fig is None:
        fig = go.Figure()

    axes_config = {
        'scaleanchor': 'x',
        'scaleratio': 1,
        'tick0': 0,
        'dtick': 1,
        'gridcolor': 'black',
        'zerolinecolor': 'black',
        'minor': {
            'dtick': 0.1,
            'gridcolor': 'gray',
            'gridwidth': 0.1
        }
    }
    if 'axes_config' in kwargs:
        ac = kwargs.pop('axes_config')
        for key, value in ac.items():
            if isinstance(axes_config[key], dict):
                axes_config[key] |= value
            else:
                axes_config[key] = value

    fig.update_xaxes(**axes_config)
    fig.update_yaxes(**axes_config)

    fig.add_trace(go.Scatter(x=np.real(init_points), y=np.imag(init_points), **kwargs))

    return fig
