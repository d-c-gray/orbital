# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 20:10:11 2023

@author: coleg
"""
class physical_float(float):
    def __new__(self, value, units):
      return float.__new__(self, value)
    def __init__(self, value:float, units:str):
      float.__init__(value)
      self.units = units


#make physical constants
G = physical_float(6.67430e-11,'m^3*kg*s^-2')