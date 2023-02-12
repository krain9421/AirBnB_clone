#!/usr/bin/python3
"""Initialization magic module for all the models"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
