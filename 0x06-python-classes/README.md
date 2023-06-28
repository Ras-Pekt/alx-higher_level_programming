## 0x06. Python - Classes and Objects
This directory contains python programs/scripts that do the following:
- [0-square.py](0-square.py) - an empty class `Square` that defines a square
- [1-square.py](1-square.py) - defines a square by: (based on [0-square.py](0-square.py))
				
				Private instance attribute: `size` 
				
				Instantiation with `size` (no type/value verification)
- [2-square.py](2-square.py) - defines a square by: (based on [1-square.py](1-square.py))
				
				Private instance attribute: `size`
				
				Instantiation with optional `size`: `def __init__(self, size=0)`
- [3-square.py](3-square.py) - defines a square by: (based on [2-square.py](2-square.py))
				
				Private instance attribute: `size`
				
				Instantiation with optional `size`: `def __init__(self, size=0)`
- [4-square.py](4-square.py) - defines a square by: (based on [3-square.py](3-square.py))

				Private instance attribute: `size`:
				
					property `def size(self):` to retrieve it
					
					property setter `def size(self, value):` to set it:
					
						`size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
						
						if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
						
				Instantiation with optional `size`: `def __init__(self, size=0):`
				
				Public instance method: def area(self): that returns the current square area