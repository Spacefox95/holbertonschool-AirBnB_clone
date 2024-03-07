#!/usr/bin/python3
"""
Module for BaseModel unittest
"""
import uuid
import os
import json
from models.base_model import BaseModel
import unittest
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def test_path(self):
        file_storage = FileStorage()
        expected_file = os.path.abspath("file.json")
        self.assertEqual(file_storage._FileStorage__file_path, expected_file)

    def test_object(self):
        file_object = FileStorage()
        self.assertIsInstance(file_object._FileStorage__objects, dict)

    def test_all(self):
        file_storage = FileStorage()
        all_objects = file_storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertIs(all_objects, file_storage._FileStorage__objects)

    def test_new(self):
        file_storage = FileStorage()
        base_model = BaseModel()
        file_storage.new(base_model)
        obj_key = "BaseModel." + base_model.id
        self.assertIn(obj_key, file_storage._FileStorage__objects)

    def test_save(self):
        file_storage = FileStorage()
        new_model = BaseModel()
        file_storage.new(new_model)
        file_storage.save()
        with open('file.json', 'r') as file:
            recup_file = json.load(file)
        self.assertIn("BaseModel." + new_model.id, recup_file)

    def test_reload(self):
        file_storage_1 = FileStorage()
        new_mod_1 = BaseModel()

        file_storage_1.new(new_mod_1)
        file_storage_1.save()
        file_storage_1.reload()

        with open("file.json", 'r') as file:
            self.assertIn("BaseModel." + new_mod_1.id, json.load(file))

        file_storage_1.save()
        file_storage_1._FileStorage__objects = {}
        file_storage_1.reload()
        self.assertNotEqual(file_storage_1.all(), {})


if __name__ == "__main__":
    unittest.main()
