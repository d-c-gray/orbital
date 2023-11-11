# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 20:50:38 2023

@author: coleg
"""

from datetime import datetime as _datetime
import pytz as _pytz
from numpy import fix as _fix
from astropy.time import *

def intdiv(a: int, b: int):
    """
    Round the a/b to nearest integer towards zero

    Parameters
    ----------
    a : int
        DESCRIPTION.
    b : int
        DESCRIPTION.

    Returns
    -------
    int
        Fixed divisor.

    """
    return _fix(a/b)


class datetime(_datetime):
    # i don't understand why this works but it does
    def __init__(self, *args,**kwargs):
        super(_datetime, self).__init__()

    def to_JD(self):
        UT = self.astimezone(_pytz.utc)
        Y = UT.year
        M = UT.month
        D = UT.day
        a = intdiv(1461 * (Y + 4800 + intdiv(M - 14,12)),4) 
        b = intdiv(367 * (M - 2 - 12 * intdiv(M - 14,12)),12) 
        c =  -intdiv(3 * (intdiv(Y + 4900 + intdiv(M - 14,12),100)),4) 
        d = D - 32075
        JDN = a+b+c+d
        JD = JDN + (UT.hour-12)/24 + UT.minute/1440 + UT.second/86400
        return JD

    def to_TBD(self):
        jd = self.to_JD()
        return Time(jd,format = 'jd').tdb.value

    # def Julian_to_JD(self):
    #     UT = self.astimezone(pytz.utc)
    #     Y = UT.year
    #     M = UT.month
    #     D = UT.day
    #     a = 367*Y
    #     # calculate julian day  number
    #     b = - intdiv(7*(Y + 5001 + intdiv((M - 9), 7)), 4)
    #     c = intdiv(275*M, 9) + D + 1729777
    #     JDN = a+b+c
    #     JD = JDN + (UT.hour-12)/24 + UT.minute/1440 + UT.second/86400
    #     return JD




if __name__ == "__main__":
    d = datetime(2000, 1, 1, 18,tzinfo = pytz.utc)
    jd = d.to_JD()
    tdb = d.to_TBD()
    print(d)
    print('JD: ',jd)
    print('TDB: ',tdb)
    
