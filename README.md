# Degenerator_Vishnyakova
It's simple json-validator, you can use it to add restrictions to fields
the program eats a json file and recursively goes through the entire structure of the json file adding the necessary parameters

HOW TO USE:
Put your json script in the input.txt file and run the program

Now default settings:
Type:
 - object
   - add: additionalProperties = False
 - string
   - add: maxLength = 255
 - array
   - add: maxItems = 100
 - number or integer
   - add: minimum = -2147483648, maximum = 2147483647
  
