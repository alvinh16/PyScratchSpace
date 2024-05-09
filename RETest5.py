#!/usr/bin/python3

import re

pattern = re.compile("[A-Za-z\s]+$")
print (pattern.search("Hello World!"))
print (pattern.search("Hello World"))
print (pattern.search("HelloWorld"))
print (pattern.search("HELLO WORLD!"))
print (pattern.search("HELLO WORLD"))
print (pattern.search("HELLOWORLD!"))
print (pattern.search("HELLOWORLD"))
