# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 17:10:41 2023

@author: coleg
"""


import numpy as np
import sys
sys.path.append(r'C:/code')
from orbital import ephemeris as ephem,plot as plt,time , planets





ephem.open_jplephem('de421', ephem.de421)

t0 = time.datetime(2023,1,1).to_TBD()
tend = t0 + 30
times = np.linspace(t0, tend, 1000)

earth = ephem.Ephemeris.from_jplephem(
    'de421',
    (0, 3),
    times,
)

sun = ephem.Ephemeris.from_jplephem(
    'de421',
    (0, 10),
    times,
)

mars = ephem.Ephemeris.from_jplephem(
    'de421',
    (0, 4),
    times,
)

moon_earthbary = ephem.Ephemeris.from_jplephem(
    'de421',
    (3, 301),
    times,
)

moon = earth+moon_earthbary

plt.close('all')
plt.orbits({
    'Earth Solar Bary':earth,
    'Sun Solar Bary':sun,
    'Mars':mars,
    'Moon':moon
    }
    )

plt.orbits(
    {'Moon':moon_earthbary}
    )