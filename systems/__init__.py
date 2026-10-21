# Game logic systems for the Solar System simulation
"""
Systems package for the Solar System simulation.

This package contains all the game logic systems:
- Planet orbital mechanics
- Lighting system for the Sun
"""

# Import and re-export main functions from planet_orbit module
from .planet_orbit import (
    update_planets,
    get_planet_orbit_info,
    reset_all_orbits
)

# Version info
__version__ = "1.0.0"
__author__ = "Solar System School Project"
__description__ = "Game logic systems for 3D Solar System simulation"

# Re-export all public symbols
__all__ = [
    # Planet orbit system
    'update_planets',
    'get_planet_orbit_info', 
    'reset_all_orbits'
]