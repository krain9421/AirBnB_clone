#!/usr/bin/python3
"""Init magic module for initializing models"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
