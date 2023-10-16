Python - Almost A Circle
Description
This project is a comprehensive review of Python programming concepts, focusing on object-oriented programming, unit testing, and serialization/deserialization. The project involves creating a set of classes that represent geometric shapes like rectangles and squares, and performing various operations on them.

Requirements
Allowed editors: vi, vim, emacs
All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All files should end with a new line
The first line of all files should be exactly #!/usr/bin/python3
Code should use the pycodestyle (version 2.8.*)
All files must be executable
All modules, classes, and functions must be documented
Tasks
0. If it's not tested it doesn't work
All your files, classes, and methods must be unit tested and be PEP 8 validated.

1. Base class
Create a class Base that will manage the id attribute for all future classes.

2. First Rectangle
Create a class Rectangle that inherits from Base.

3. Validate attributes
Update the class Rectangle by adding validation of all setter methods and instantiation.

4. Area first
Add a method that returns the area value of the Rectangle instance.

5. Display #0
Add a method that prints the Rectangle instance with the character #.

6. str
Override the __str__ method for the Rectangle class.

7. Display #1
Improve the display method to take care of x and y.

8. Update #0
Add a method that assigns an argument to each attribute.

9. Update #1
Update the update method to accept key-value arguments.

10. And now, the Square!
Create a class Square that inherits from Rectangle.

11. Square size
Add a public getter and setter for the size attribute.

12. Square update
Add a method that assigns attributes for the Square class.

13. Rectangle instance to dictionary representation
Add a method that returns the dictionary representation of a Rectangle.

14. Square instance to dictionary representation
Add a method that returns the dictionary representation of a Square.

15. Dictionary to JSON string
Add a static method that returns the JSON string representation of a list of dictionaries.

16. JSON string to file
Add a class method that writes the JSON string representation of a list of objects to a file.

17. JSON string to dictionary
Add a static method that returns the list of the JSON string representation.

18. Dictionary to Instance
Add a class method that returns an instance with all attributes already set.

19. File to instances
Add a class method that returns a list of instances.

Usage
Each task has its own test file which can be run to check the functionality of the classes and methods.
