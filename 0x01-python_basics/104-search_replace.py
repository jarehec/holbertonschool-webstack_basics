#!/usr/bin/python3
"""
module containing search_replace function
"""


def search_replace(my_list, search, replace):
    """
    replaces all occurrences of an element by another in a new list
    @my_list: initial list
    @search: element to replace
    @element: new element
    """
    new_list = my_list.copy()
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
