#!/usr/bin/python3
"""Init module for models"""
from models.engine.file_storage import FileStorage


# Create an instance of FileStorage
storage = FileStorage()
storage.reload()
