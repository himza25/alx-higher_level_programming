#!/usr/bin/python3
"""This module defines the Base class"""

import json
import csv


class Base:
    """The Base class serves as the 'base' for all other classes in this
    project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_dictionary(self):
        """Returns the dictionary representation of a Base object"""
        return {'id': self.id}

    # Task 15
    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    # Task 16 and 20
    @classmethod
    def save_to_file(cls, list_objs):
        """Save the JSON string representation of list_objs to a file."""
        list_dicts = []
        if list_objs is not None:
            list_dicts = [o.to_dictionary() for o in list_objs]
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(list_dicts))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves a list of Rectangle or Square objects to a CSV file."""
        filename = "{}.csv".format(cls.__name__)
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y]
                    )
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

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
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    # Task 19 and 20
    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                list_dicts = cls.from_json_string(f.read())
            return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """Loads a list of Rectangle or Square objects from a CSV file."""
        filename = "{}.csv".format(cls.__name__)
        list_objs = []
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])
                        }
                        list_objs.append(cls.create(**dictionary))
                    elif cls.__name__ == "Square":
                        dictionary = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])
                        }
                        list_objs.append(cls.create(**dictionary))
            return list_objs
        except FileNotFoundError:
            return []

    # Task 21
    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draws all Rectangles and Squares using Turtle graphics. """
        import turtle

        turtle.speed(1)

        for rect in list_rectangles:
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.right(90)
                turtle.forward(rect.height)
                turtle.right(90)
            turtle.penup()
            turtle.forward(rect.width + 10)
            turtle.pendown()

        turtle.penup()
        turtle.goto(0, -100)
        turtle.pendown()

        for square in list_squares:
            for _ in range(4):
                turtle.forward(square.size)
                turtle.right(90)
            turtle.penup()
            turtle.forward(square.size + 10)
            turtle.pendown()

            turtle.done()
