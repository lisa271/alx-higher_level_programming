#!/usr/bin/python3
"""defining write_file with two arguments"""

def write_file(filename="", text=""):
    with open(filename, "w", encoding = 'utf-8') as f:
        return f.write("Writes file with two arguments\n")
