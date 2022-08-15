from __future__ import annotations
from typing import Optional
from numbers import Number

class _Node:

    def __init__(self, value=None, parent:_Node=None) -> None:
        assert value != None, "No value given!"
        assert isinstance(value, Number), "Value given must be a number!"
        self._left_child = None
        self._right_child = None
        self._parent = parent
        self._value = value

    def set_left_child(self, child:_Node=None) -> None:
        assert isinstance(child, _Node) or\
                child == None, "Bad child type!"

        self._left_child = child

    def set_right_child(self, child:_Node=None) -> None:
        assert isinstance(child, _Node) or\
                child == None, "Bad child type!"

        self._right_child = child

    def set_parent(self, parent:_Node=None) -> None:
        assert isinstance(parent, _Node) or\
                parent == None, "Bad parent type!"

        self._parent = parent

    def get_left_child(self) -> Optional[_Node]:
        return self._left_child

    def get_right_child(self) -> Optional[_Node]:
        return self._right_child

    def get_parent(self) -> Optional[_Node]:
        return self._parent

    def get_value(self) -> Number:
        return self._value

class BST:

    def __init__(self) -> None:
        self._root_node = None

    def insert(self):
        pass

    def find(self):
        pass

    def delete(self):
        pass
