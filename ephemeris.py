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

def open_jplephem(
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

    def __init__(self,
                 position,
                 velocity,
                 timestamps,
                 ):
        self.p = position
        self.v = velocity
        self.t = timestamps



    @classmethod
    def from_jplephem(
            cls,
            kernel_name: str,
            index: tuple[int],
            times: _np.ndarray,
            ):
        try:
            kernel = jplkernels[kernel_name]
        except KeyError:
            raise Exception(' Must open_jplephem(name) first')

        seg = kernel[index[0],index[1]]
        pos,vel = seg.compute_and_differentiate(times)
        obj = cls.__new__(cls)
        cls.__init__(
            obj,
            pos,
            vel,
            times
            )
        return obj

    def __add__(self,o):
        p = self.p+o.p
        t = self.t
        v = self.v + o.v
        return Ephemeris(p,v,t)

    def __sub__(self,o):
        p = self.p - o.p
        t = self.t
        v = self.v - o.v
        return Ephemeris(p,v,t)


if __name__ == "__main__":
    open_jplephem('de421', r'ephemerides/de421.bsp')

    earth = Ephemeris.from_jplephem(
        'de421',
        (0,3),
        2425854,
        )