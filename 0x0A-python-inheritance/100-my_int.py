#!/usr/bin/python3
class MyInt(int):
    """Rebel integer class"""

    def __eq__(self, other):
        """Override equality operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override inequality operator"""
        return super().__eq__(other)
