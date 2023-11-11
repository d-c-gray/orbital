# -*- coding: utf-8 -*-
"""
Contains information relating to solar bodies
"""
import pandas as _pd
from os.path import dirname as _dir, join as _join
from argparse import Namespace

class physical_float(float):
    def __new__(self, value, units):
      return float.__new__(self, value)
    def __init__(self, value:float, units:str):
      float.__init__(value)
      self.units = units

class Body():
    def __init__(
            self,
            mass: float,
            mean_radius: float,
            ):
        self.mass = physical_float(mass,'kg')
        self.mean_radius = physical_float(mean_radius,'m')

#make physical constants
G = physical_float(6.67430e-11,'m^3*kg*s^-2')

#celestial bodies
_d = _join(_dir(__file__),'body_data')
_planets = _pd.read_csv(_join(_d,'planets.csv'),index_col=0)

_pdict = {}
for p in _planets.index:
    if p != 'Planet' and p!='Units':
        mass = float(_planets.loc[p]['Mass'].replace(',',''))*1e24
        mean_radius = float(_planets.loc[p]['Mean\nRadius'].replace(',',''))*1000
        _pdict[p]=Body(mass,mean_radius)

planets = Namespace(**_pdict)

