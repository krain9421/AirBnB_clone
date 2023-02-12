#!/usr/bin/python3
"""Initialization magic module that
    creates a FileStorage object for storage
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
