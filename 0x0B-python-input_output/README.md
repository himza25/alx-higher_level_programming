# alx-higher_level_programming - Python Input/Output

This repository contains Python scripts that demonstrate various input and output operations.

## Files

### 0-read_file.py

This script defines a function `read_file(filename="")` that reads a text file (UTF8) and prints its content to stdout. It uses the `with` statement for proper file handling and does not handle file permission or file not found exceptions. No external modules are imported.

### 1-write_file.py

This script defines a function `write_file(filename="", text="")` that writes a string to a text file (UTF8) and returns the number of characters written. It uses the `with` statement for proper file handling, creates the file if it doesn't exist, and overwrites the content if the file already exists. No external modules are imported.

### 2-append_write.py

This script defines a function `append_write(filename="", text="")` that appends a string to the end of a text file (UTF8) and returns the number of characters added. If the file doesn't exist, it is created. It uses the `with` statement for proper file handling and does not handle file permission or file not found exceptions. No external modules are imported.

### 3-to_json_string.py

This script defines a function `to_json_string(my_obj)` that returns the JSON representation of an object as a string. It does not handle exceptions if the object cannot be serialized to JSON. No external modules are imported.

### 4-from_json_string.py

This script defines a function `from_json_string(my_str)` that returns an object (Python data structure) represented by a JSON string. It does not handle exceptions if the JSON string is invalid. No external modules are imported.

### 5-save_to_json_file.py

This script defines a function `save_to_json_file(my_obj, filename)` that writes an object to a text file using its JSON representation. It uses the `with` statement for proper file handling and does not handle exceptions if the object cannot be serialized. No external modules are imported.

### 6-load_from_json_file.py

This script defines a function `load_from_json_file(filename)` that creates an object from a JSON file. It uses the `with` statement for proper file handling and does not handle file not found exceptions. No external modules are imported.

### 7-add_item.py

This script defines a script that adds command-line arguments to a Python list and saves them to a file in JSON format. It uses the `save_to_json_file` and `load_from_json_file` functions defined earlier. It does not handle exceptions for invalid JSON files. No external modules are imported.

### 8-class_to_json.py

This script defines a function `class_to_json(obj)` that returns a dictionary description of a class instance with simple data structures (list, dictionary, string, integer, and boolean) suitable for JSON serialization. No external modules are imported.

### 9-student.py

This script defines a class `Student` with public instance attributes `first_name`, `last_name`, and `age`. It also defines a `to_json` method that retrieves a dictionary representation of a `Student` instance. No external modules are imported.

### 10-student.py

This script extends the `Student` class to include a `to_json` method that can filter the attributes to include in the dictionary representation. It accepts a list of attribute names as an argument. No external modules are imported.

### 11-student.py

This script further extends the `Student` class to include a `reload_from_json` method that replaces all attributes of the `Student` instance based on a provided dictionary. No external modules are imported.

### 12-pascal_triangle.py

This script defines a function `pascal_triangle(n)` that returns a list of lists of integers representing Pascal's triangle up to the nth row. It does not import external modules and returns an empty list for n <= 0.

### 100-append_after.py

This script defines a function `append_after(filename="", search_string="", new_string="")` that inserts a line of text into a file after each line containing a specific search string.

### 101-stats.py

This script reads input lines in a specific format from stdin and computes metrics, including total file size and the count of lines for each HTTP status code. It prints the statistics every 10 lines or upon receiving a keyboard interruption (CTRL + C).
