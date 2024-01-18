"""
Database package created for Ambitify
Allows you to work with the user's schedule
© Andboogl, 2024
"""


from .database import Database
from . import errors


__all__ = ['Database', 'errors']
