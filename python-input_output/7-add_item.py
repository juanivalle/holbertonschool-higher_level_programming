#!/usr/bin/python3
"""Load, add, save"""


import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
try:
    list_ = load_from_json_file(filename)
except FileNotFoundError:
    list_ = []
for i in range(1, len(sys.argv)):
    list_.append(sys.argv[i])
save_to_json_file(list_, filename)
