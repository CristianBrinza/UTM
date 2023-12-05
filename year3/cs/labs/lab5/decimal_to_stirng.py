# python3 decimal_to_stirng.py

decimal_values = [67,114,105,115,116,105,97,110,32,66,114,105,110,122,97]
ascii_string = ''.join(chr(num) for num in decimal_values)
print(ascii_string)