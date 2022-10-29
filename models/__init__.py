#!/usr/bin/python3
"""initialising the models package"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
