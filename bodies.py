# -*- coding: utf-8 -*-
"""
Contains information relating to solar bodies
"""
import pandas as _pd
import numpy as _np
from os.path import dirname as _dir, join as _join
from argparse import Namespace as _Namespace
from  .const import G,physical_float as _pfloat


class Body():
    """
    A physical body to be included in a simulation
    """
    def __init__(self,
                 ephemeral: bool,
                 massive: bool,
                 ):
        self.ephemeral = ephemeral
        self.massive = massive
        pass

class MassiveSphericalCelestial(Body):
    """
    A massive body whose movement is prescribed by an ephemeris data set
    """
    def __init__(
            self,
            GM: float,
            mean_radius: float,
            ephemeris = None,
            ):
        self.GM = GM
        self.mean_radius = _pfloat(mean_radius,'km')
        self.ephemeris = ephemeris
        Body.__init__(self,ephemeral = True, massive =  True)

    def set_ephemeris(self,ephemeris):
        self.ephemeris = ephemeris

    def __getitem__(self,t):
            return self.ephemeris[t]


class Craft(Body):
    def __init__(self, massive:bool = False):
        Body.__init__(self,ephemeral = False,massive = massive,)
        self.m = _np.array([],dtype = float)
        self.t = _np.array([],dtype = float)
        self.p  = _np.empty((1,3),dtype = float)
        self.v = _np.empty((1,3),dtype = float)
        pass



#celestial bodies
_d = _join(_dir(__file__),'body_data')
#planetary data
_planets = _pd.read_csv(_join(_d,'planets.csv'),index_col=0)

_pdict = {}
for p in _planets.index:
    if p != 'Planet' and p!='Units':
        GM = G*float(_planets.loc[p]['Mass'].replace(',',''))*1e24
        mean_radius = float(_planets.loc[p]['Mean\nRadius'].replace(',',''))*1000
        _pdict[p]=MassiveSphericalCelestial(GM,mean_radius)

planets = _Namespace(**_pdict)

_sats = _pd.read_csv(_join(_d,'satellites.csv'),index_col=0)

_sdict = {}
for s in _sats.index:
    GM = float(_sats.loc[s]['GM (km3/s2)'])*1e9
    mean_radius = float(_sats.loc[s]['Mean Radius (km)'])*1000
    _sdict[s]=MassiveSphericalCelestial(GM,mean_radius)

satellites = _Namespace(**_sdict)


