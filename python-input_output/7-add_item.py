#!/usr/bin/python3
"""Load, add, save"""


import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
objeto = [arg for arg in sys.argv if arg != sys.argv[0]]
try:
    py_list = load_from_json_file(filename)
except FileNotFoundError:
    save_to_json_file(objeto, filename)
else:
    for i in objeto:
    py_lsit.append(i)
    save_to_json_file(py_list, filename)
