# -*- coding: utf-8 -*-

from __future__ import division

from .conversions import CT_from_pt
from ..utilities import match_args_return


__all__ = ['latentheat_evap_t']
#           'latentheat_evap_CT',
#           'latentheat_melting',


#@match_args_return
#def latentheat_evap_CT(SA, CT):
#    pass


#@match_args_return
#def latentheat_melting(SA, p):
#    pass


@match_args_return
def latentheat_evap_t(SA, t):
    """
    Calculates latent heat, or enthalpy, of evaporation at p = 0 (the
    surface).  It is defined as a function of Absolute Salinity, SA, and
    in-situ temperature, t, and is valid in the ranges 0 < SA < 40 g/kg and
    0 < CT < 42 deg C.  The errors range between -0.4 and 0.6 J/kg.

    Parameters
    ----------
    SA : array_like
         Absolute salinity [g kg :sup:`-1`]
    t : array_like
        in situ temperature [:math:`^\circ` C (ITS-90)]

    Returns
    -------
    latentheat_evap_t : array_like
        latent heat of evaporation [J kg :sup:`-1`]

    References
    ----------
    .. [1] IOC, SCOR and IAPSO, 2010: The international thermodynamic equation
       of seawater - 2010: Calculation and use of thermodynamic properties.
       Intergovernmental Oceanographic Commission, Manuals and Guides No. 56,
       UNESCO (English), 196 pp. See section 3.39.
    """

    CT = CT_from_pt(SA, t)
    return latentheat_evap_CT(SA, CT)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
