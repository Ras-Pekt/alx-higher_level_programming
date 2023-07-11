## 0x0B. Python - Input/Output
This directory contains python programs/scripts that do the following:
- [0-read_file.py](0-read_file.py) - reads a text file (UTF8) and prints it to stdout
- [1-write_file.py](1-write_file.py) - writes a string to a text file (UTF8) and returns the number of characters written
- [2-append_write.py](2-append_write.py) - appends a string at the end of a text file (UTF8) and returns the number of characters added
- [3-to_json_string.py](3-to_json_string.py) - returns the JSON representation of an object (string)
- [4-from_json_string.py](4-from_json_string.py) - returns an object (Python data structure) represented by a JSON string
- [5-save_to_json_file.py](5-save_to_json_file.py) - writes an Object to a text file, using a JSON representation
- [6-load_from_json_file.py](6-load_from_json_file.py) - creates an Object from a “JSON file”
- [7-add_item.py](7-add_item.py) - adds all arguments to a Python list, and then save them to a file
- [8-class_to_json.py](8-class_to_json.py) - returns the dictionary description with simple data structure for JSON serialization of an object
- [9-student.py](9-student.py) - a class Student that defines a student by:
	- Public instance attributes
	- Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
	- Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance