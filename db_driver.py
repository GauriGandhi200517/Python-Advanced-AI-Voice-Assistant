import sqlite3
from typing import Optional
from dataclasses import dataclass
from contextlib import contextmanager

from backend.db_driver import *  # re-export moved backend implementation