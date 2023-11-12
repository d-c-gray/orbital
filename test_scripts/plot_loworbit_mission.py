# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 20:36:20 2023

@author: coleg
"""

from orbital import ephemeris,Ephemeris, planets, satellites, plot, time
import numpy as np
import sys
sys.path.append(r'C:/code')


ephemeris.open_jplkernel('de421', ephemeris.de421)

# get earth/lunar ephemeris in earth barycentric ref frame
# indexes come from printing the opened 'de421' kernel
# print(ephemeris.jplkernels['de421'])
# >>File type DAF/SPK and format LTL-IEEE with 15 segments:
# >>2414864.50..2471184.50  Type 2  Solar System Barycenter (0) -> Mercury Barycenter (1)
# >>2414864.50..2471184.50  Type 2  Solar System Barycenter (0) -> Venus Barycenter (2)
# >>2414864.50..2471184.50  Type 2  Solar System Barycenter (0) -> Earth Barycenter (3)
# >>2414864.50..2471184.50  Type 2  Solar System Barycenter (0) -> Mars Barycenter (4)
# >>2414864.50..2471184.50  Type 2  Solar System Barycenter (0) -> Jupiter Barycenter (5)
# >>2414864.50..2471184.50  Type 2  Solar System Barycenter (0) -> Saturn Barycenter (6)
# >>2414864.50..2471184.50  Type 2  Solar System Barycenter (0) -> Uranus Barycenter (7)
# >>2414864.50..2471184.50  Type 2  Solar System Barycenter (0) -> Neptune Barycenter (8)
# >>2414864.50..2471184.50  Type 2  Solar System Barycenter (0) -> Pluto Barycenter (9)
# >>2414864.50..2471184.50  Type 2  Solar System Barycenter (0) -> Sun (10)
# >>2414864.50..2471184.50  Type 2  Earth Barycenter (3) -> Moon (301)
# >>2414864.50..2471184.50  Type 2  Earth Barycenter (3) -> Earth (399)
# >>2414864.50..2471184.50  Type 2  Mercury Barycenter (1) -> Mercury (199)
# >>2414864.50..2471184.50  Type 2  Venus Barycenter (2) -> Venus (299)
# >>2414864.50..2471184.50  Type 2  Mars Barycenter (4) -> Mars (499)

# p_const/v_const are multiplied by output of kernels when indexing into a time
# this kernel provided units in KM and KM/Day, and I want to convert to m and m/s

earthbary2earth = Ephemeris.from_jpl('de421', (3, 399),p_const = 1000, v_const = 1/(24*3600))

earthbary2moon = Ephemeris.from_jpl('de421', (3, 301),p_const = 1000, v_const = 1/(24*3600))

# get lunar ephemeris in earth center reference frame
earth2moon = earthbary2moon - earthbary2earth

# determine mission start time
# de421 uses Barycentric Dynamic Time, so convert to that
t0 = time.datetime(2025, 6, 29, hour=12).to_TBD()

# assign ephemeris data to Earth and Moon
# Using an Earth centric coordiante frame, so assigning it as origin
# this just makes it output [0] vectors for position/velocity
satellites.Moon.set_ephemeris(earth2moon)
planets.Earth.set_ephemeris(Ephemeris.as_origin())


