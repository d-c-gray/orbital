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

earth = ephem.Ephemeris.from_jplephem('de421',(0, 3))

sun = ephem.Ephemeris.from_jplephem('de421',(0, 10))

mars = ephem.Ephemeris.from_jplephem('de421',(0, 4))

moon_earthbary = ephem.Ephemeris.from_jplephem('de421',(3, 301))

earth_earthbary = ephem.Ephemeris.from_jplephem('de421',(3, 399))

moon = earth+moon_earthbary

plt.close('all')
plt.orbits(
    times,
    {
    'Earth Solar Bary':earth,
    'Sun Solar Bary':sun,
    'Mars':mars,
    'Moon':moon
    }
    )

plt.orbits(
    times,
    {'Moon':moon_earthbary,
    'Earth':earth_earthbary
    }
    )