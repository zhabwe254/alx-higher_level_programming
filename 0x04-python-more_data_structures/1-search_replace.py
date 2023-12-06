#!/usr/bin/python3

def search_replace(my_list, search, replace):
"""
Replaces all occurrences of an element in a list.

Args:
my_list: The list to search in.
search: The element to replace.
replace: The replacement element.

Returns:
A new list with replaced elements.
"""
return [replace if element == search else element for element in my_list]
```
