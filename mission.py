# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 15:28:42 2023

@author: coleg
"""
from numpy import _np
from physical import *
from ephemeris import *
from scipy.integrate import RK45

class Leg():
    def __init__(self,
        t0: float,
        craft: float,
        bodies: float,
        ):

        self.t0 = t0
        self.craft = craft
        self.bodies = bodies

    def compute(
            max_time: float,
            first_step = None,
            max_step = None,
            stop_condition = None,
            ):
        p0,v0 = self.craft[t0]
        y0 = np.extend(p0,y0)
        solver = RK45(
                    self. newton_point_mass,
                    self.t0,
                    y0,
                    max_time
                    )

        computing = True
        while computing:
            msg = solver.step()


    @classmethod
    def newton_point_mass(self,t,y):
        
        a = np.array([0,0,0])
        for b in self.bodies:
            p,v = b[t]
            delta = y[0:3]-p
            magr3 = np.sqrt(np.sum(delta**2))**3
            a+= b.GM*delta/magr3
        ydot = np.extend(y[3:6],a)
        return ydot


