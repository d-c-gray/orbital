# -*- coding: utf-8 -*-
"""
Contains definitions 
"""
import numpy as _np

from jplephem.spk import SPK as _SPK
from os.path import dirname as _dirname,join as _join

_ephempath = _join(_dirname(__file__),'ephemerides')
de421 =  _join(_ephempath,'de421.bsp')

jplkernels = {}

def open_jplkernel(
    name:str,
    file:str,
    ):
    jplkernels[name] = _SPK.open(file)



def close_jplkernel(name:str):
    if name == 'all':
        for v in jplkernels.values():
            v.close()
        return
    else:
        jplkernels[name].close()


class Ephemeris():

    def __init__(self,fun):
        """
        Create an Ephemeris object.
        
        Ephemeris objects take in a time index (float or array) and return
        a tuple of position and velocity objects.

        Parameters
        ----------
        fun : obj
            The kernel function that takes in a time and returns the position
            and velocity of the object.

        """
        self.kernel = fun
        
        

    @classmethod
    def as_origin(cls):
        def fun(t):
            if type(t) is _np.ndarray and len(t) > 1:
                return _np.zeros((len(t)),3,float),_np.zeros((len(t)),3,float)
            else:
                return _np.zeros((3,),float),_np.zeros((3,),float)
            
        obj = cls.__new__(cls)
        cls.__init__(obj,fun)
        return obj

    @classmethod
    def from_jpl(
            cls,
            kernel_name: str,
            index: tuple[int],
            p_const: float = 1,
            v_const:float =  1
            ):
        try:
            kernel = jplkernels[kernel_name]
        except KeyError:
            raise Exception(' Must open_jplephem(name) first')

        seg = kernel[index[0],index[1]]
        def get(times):
            pos,vel = seg.compute_and_differentiate(times)
            return pos*p_const,vel*v_const
        obj = cls.__new__(cls)
        cls.__init__(obj,get)
        return obj

    @classmethod
    def from_numpy(
            t,
            p,
            v
            ):
        pass

    def __getitem__(self,t):
        return self.kernel(t)

    def __add__(self,o):
        def get(t):
            p1,v1 = self[t]
            p2,v2 = o[t]
            return p1-p2,v1-v2
        
        return Ephemeris(get)

    def __sub__(self,o):
        def get(t):
            p1,v1 = self[t]
            p2,v2 = o[t]
            return p1-p2,v1-v2
        
        return Ephemeris(get)


if __name__ == "__main__":
    open_jplkernel('de421', r'ephemerides/de421.bsp')

    earth = Ephemeris.from_jpl('de421',(0,3))
    mars = Ephemeris.from_jpl('de421',(0,4))

    p1,v1 = earth[2460000]
    p2,v2 = mars[2460000]
    e2m = mars-earth
    p2m,v2m = e2m[2460000]
    print(p2m- (p2-p1))