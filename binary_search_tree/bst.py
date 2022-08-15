from __future__ import annotations
from typing import Optional

class _Node:

    def __init__(self, parent:_Node=None) -> None:

        self._left_child = None
        self._right_child = None
        self._parent = parent

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

class BST:

    def __init__(self) -> None:
        pass

    def insert(self):
        pass

    def find(self):
        pass

    def delete(self):
        pass
