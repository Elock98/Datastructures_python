import unittest

from bst import BST
from bst import _Node
from unittest.mock import patch

class TestNode(unittest.TestCase):

#-------------------------------------------------------------------#

    def test_create_root(self):
        # Given / When
        node = _Node(1)

        # Then
        self.assertEqual(node._value, 1)
        self.assertEqual(node._left_child, None)
        self.assertEqual(node._right_child, None)
        self.assertEqual(node._parent, None)


    def test_create(self):
        # Given
        root_node = _Node(1)

        # When
        node = _Node(2, root_node)

        # Then
        self.assertEqual(node._value, 2)
        self.assertEqual(node._parent._value, 1)
        self.assertEqual(node._left_child, None)
        self.assertEqual(node._right_child, None)
        self.assertEqual(node._parent, root_node)

    def test_create_no_value(self):
        # Given / When
        with self.assertRaises(Exception) as ex:
            node = _Node()

        # Then
        self.assertEqual(str(ex.exception), "No value given!")

    def test_create_bad_value(self):
        # Given / When
        with self.assertRaises(Exception) as ex:
            node = _Node("foo")

        # Then
        self.assertEqual(str(ex.exception), "Value given must be a number!")

#-------------------------------------------------------------------#

    def test_set_left_child(self):
        # Given
        node = _Node(1)
        child_node = _Node(2, node)

        # When
        node.set_left_child(child_node)

        # Then
        self.assertEqual(node._left_child, child_node)
        self.assertEqual(child_node._parent, node)

    def test_set_left_child_to_none(self):
        # Given
        node = _Node(1)
        child_node = _Node(2, node)

        # When
        node.set_left_child(None)

        # Then
        self.assertEqual(node._left_child, None)
        self.assertEqual(child_node._parent, node)

    def test_set_left_child_no_param(self):
        # Given
        node = _Node(1)
        child_node = _Node(2, node)

        # When
        node.set_left_child()

        # Then
        self.assertEqual(node._left_child, None)
        self.assertEqual(child_node._parent, node)

    def test_set_left_child_bad_param(self):
        # Given
        node = _Node(1)
        child_node = _Node(2, node)

        # When
        with self.assertRaises(Exception) as ex:
            node.set_left_child("baz")

        # Then
        self.assertEqual(str(ex.exception), "Bad child type!")
        self.assertEqual(node._left_child, None)

#-------------------------------------------------------------------#

    def test_set_right_child(self):
        # Given
        node = _Node(1)
        child_node = _Node(2, node)

        # When
        node.set_right_child(child_node)

        # Then
        self.assertEqual(node._right_child, child_node)
        self.assertEqual(child_node._parent, node)

    def test_set_right_child_to_none(self):
        # Given
        node = _Node(1)
        child_node = _Node(2, node)

        # When
        node.set_right_child(None)

        # Then
        self.assertEqual(node._right_child, None)
        self.assertEqual(child_node._parent, node)

    def test_set_right_child_no_param(self):
        # Given
        node = _Node(1)
        child_node = _Node(2, node)

        # When
        node.set_right_child()

        # Then
        self.assertEqual(node._right_child, None)
        self.assertEqual(child_node._parent, node)

    def test_set_right_child_bad_param(self):
        # Given
        node = _Node(1)
        child_node = _Node(2, node)

        # When
        with self.assertRaises(Exception) as ex:
            node.set_left_child("baz")

        # Then
        self.assertEqual(str(ex.exception), "Bad child type!")
        self.assertEqual(node._left_child, None)

#-------------------------------------------------------------------#

    def test_set_parent(self):
        # Given
        parent = _Node(1)
        child = _Node(2)
        parent.set_left_child(child)

        # When
        child.set_parent(parent)

        # Then
        self.assertEqual(child._parent, parent)

    def test_set_parent_to_none(self):
        # Given
        child = _Node(1)

        # When
        child.set_parent(None)

        # Then
        self.assertEqual(child._parent, None)

    def test_set_parent_no_param(self):
        # Given
        child = _Node(2)

        # When
        child.set_parent()

        # Then
        self.assertEqual(child._parent, None)

    def test_set_parent_bad_param(self):
        # Given
        child = _Node(1)

        # When
        with self.assertRaises(Exception) as ex:
            child.set_parent("bar")

        # Then
        self.assertEqual(str(ex.exception), "Bad parent type!")
        self.assertEqual(child._parent, None)

#-------------------------------------------------------------------#

    def test_get_left_child(self):
        # Given
        node = _Node(1)
        child = _Node(2)
        node._left_child = child

        # When
        got = node.get_left_child()

        # Then
        self.assertEqual(got, child)

    def test_get_right_child(self):
        # Given
        node = _Node(1)
        child = _Node(2)
        node._right_child = child

        # When
        got = node.get_right_child()

        # Then
        self.assertEqual(got, child)

    def test_get_parent(self):
        # Given
        parent = _Node(1)
        child = _Node(2, parent)
        parent._left_child = child

        # When
        got = child.get_parent()

        # Then
        self.assertEqual(got, parent)

    def test_get_value(self):
        # Given
        node = _Node(1)

        # When
        nr = node.get_value()

        # Then
        self.assertEqual(nr, 1)

#-------------------------------------------------------------------#

class TestBST(unittest.TestCase):

#-------------------------------------------------------------------#

    def test_create(self):
        # Given / When
        bts = BST()

        # Then
        self.assertEqual(bts._root_node, None)

#-------------------------------------------------------------------#


if __name__ == "__main__":
    unittest.main()