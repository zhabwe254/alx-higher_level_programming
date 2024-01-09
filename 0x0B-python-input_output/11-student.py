#!/usr/bin/python3
"""Module for defining a student class, saving it to disk, and reloading it"""


class Student:
    """Defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of a Student instance."""
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance with values from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
