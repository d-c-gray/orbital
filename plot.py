# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 17:25:19 2023

@author: coleg
"""

from matplotlib.pyplot import *

def orbits(t,
        bodies: dict,
        ax=None,
        **plt_kwargs
):
    if ax is None:
        fig, ax = subplots(subplot_kw=dict(projection='3d'))

    for n,b in bodies.items():
        p,v = b[t]
        ax.plot(p[0, :],
                p[1, :],
                p[2, :],
                label=n,
                **plt_kwargs)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend(loc='best')
    return ax
