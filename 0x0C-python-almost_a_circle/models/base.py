#!/usr/bin/python3
"""This module defines the Base class"""


class Base:
    """The Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # Task 15
    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    # Task 16
    @classmethod
    def save_to_file(cls, list_objs):
        """Save the JSON string representation of list_objs to a file."""
        list_dicts = []
        if list_objs is not None:
            list_dicts = [o.to_dictionary() for o in list_objs]
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(list_dicts))

    # Task 17
    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    # Task 18
    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        dummy = cls(1, 1)  # Replace with your own "dummy" attributes
        dummy.update(**dictionary)
        return dummy

    # Task 19
    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                list_dicts = cls.from_json_string(f.read())
            return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
