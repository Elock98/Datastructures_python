import unittest

from bst import BST
from bst import _Node
from unittest.mock import patch

class TestNode(unittest.TestCase):

#-------------------------------------------------------------------#

    def test_create_root(self):
        # Given / When
        node = _Node(1, "foo")

        # Then
        self.assertEqual(node._value, "foo")
        self.assertEqual(node._key, 1)
        self.assertEqual(node._left_child, None)
        self.assertEqual(node._right_child, None)
        self.assertEqual(node._parent, None)


    def test_create(self):
        # Given
        root_node = _Node(1, "foo")

        # When
        node = _Node(2, "bar", root_node)

        # Then
        self.assertEqual(node._value, "bar")
        self.assertEqual(node._key, 2)
        self.assertEqual(node._parent._value, "foo")
        self.assertEqual(node._parent._key, 1)
        self.assertEqual(node._left_child, None)
        self.assertEqual(node._right_child, None)
        self.assertEqual(node._parent, root_node)

    def test_create_no_value(self):
        # Given / When
        with self.assertRaises(Exception) as ex:
            node = _Node(key=5)

        # Then
        self.assertEqual(str(ex.exception), "No value given!")

    def test_create_no_key(self):
        # Given / When
        with self.assertRaises(Exception) as ex:
            node = _Node(value="foo")

        # Then
        self.assertEqual(str(ex.exception), "No key given!")

    def test_create_bad_key(self):
        # Given / When
        with self.assertRaises(Exception) as ex:
            node = _Node(key="foo", value="bar")

        # Then
        self.assertEqual(str(ex.exception), "Key given must be a number!")

#-------------------------------------------------------------------#

    def test_set_left_child(self):
        # Given
        node = _Node(1, "foo")
        child_node = _Node(2, "bar", node)

        # When
        node.set_left_child(child_node)

        # Then
        self.assertEqual(node._left_child, child_node)
        self.assertEqual(child_node._parent, node)

    def test_set_left_child_to_none(self):
        # Given
        node = _Node(1, "foo")
        child_node = _Node(2, "bar", node)

        # When
        node.set_left_child(None)

        # Then
        self.assertEqual(node._left_child, None)
        self.assertEqual(child_node._parent, node)

    def test_set_left_child_no_param(self):
        # Given
        node = _Node(1, "foo")
        child_node = _Node(2, "bar", node)

        # When
        node.set_left_child()

        # Then
        self.assertEqual(node._left_child, None)
        self.assertEqual(child_node._parent, node)

    def test_set_left_child_bad_param(self):
        # Given
        node = _Node(1, "foo")
        child_node = _Node(2, "bar", node)

        # When
        with self.assertRaises(Exception) as ex:
            node.set_left_child("baz")

        # Then
        self.assertEqual(str(ex.exception), "Bad child type!")
        self.assertEqual(node._left_child, None)

#-------------------------------------------------------------------#

    def test_set_right_child(self):
        # Given
        node = _Node(1, "foo")
        child_node = _Node(2, "bar", node)

        # When
        node.set_right_child(child_node)

        # Then
        self.assertEqual(node._right_child, child_node)
        self.assertEqual(child_node._parent, node)

    def test_set_right_child_to_none(self):
        # Given
        node = _Node(1, "foo")
        child_node = _Node(2, "bar", node)

        # When
        node.set_right_child(None)

        # Then
        self.assertEqual(node._right_child, None)
        self.assertEqual(child_node._parent, node)

    def test_set_right_child_no_param(self):
        # Given
        node = _Node(1, "foo")
        child_node = _Node(2, "bar", node)

        # When
        node.set_right_child()

        # Then
        self.assertEqual(node._right_child, None)
        self.assertEqual(child_node._parent, node)

    def test_set_right_child_bad_param(self):
        # Given
        node = _Node(1, "foo")
        child_node = _Node(2, "bar", node)

        # When
        with self.assertRaises(Exception) as ex:
            node.set_left_child("baz")

        # Then
        self.assertEqual(str(ex.exception), "Bad child type!")
        self.assertEqual(node._left_child, None)

#-------------------------------------------------------------------#

    def test_set_parent(self):
        # Given
        parent = _Node(1, "foo")
        child = _Node(2, "bar")
        parent.set_left_child(child)

        # When
        child.set_parent(parent)

        # Then
        self.assertEqual(child._parent, parent)

    def test_set_parent_to_none(self):
        # Given
        child = _Node(1, "foo")

        # When
        child.set_parent(None)

        # Then
        self.assertEqual(child._parent, None)

    def test_set_parent_no_param(self):
        # Given
        child = _Node(2, "foo")

        # When
        child.set_parent()

        # Then
        self.assertEqual(child._parent, None)

    def test_set_parent_bad_param(self):
        # Given
        child = _Node(1, "foo")

        # When
        with self.assertRaises(Exception) as ex:
            child.set_parent("bar")

        # Then
        self.assertEqual(str(ex.exception), "Bad parent type!")
        self.assertEqual(child._parent, None)

#-------------------------------------------------------------------#

    def test_get_left_child(self):
        # Given
        node = _Node(1, "foo")
        child = _Node(2, "bar")
        node._left_child = child

        # When
        got = node.get_left_child()

        # Then
        self.assertEqual(got, child)

    def test_get_right_child(self):
        # Given
        node = _Node(1, "foo")
        child = _Node(2, "bar")
        node._right_child = child

        # When
        got = node.get_right_child()

        # Then
        self.assertEqual(got, child)

    def test_get_parent(self):
        # Given
        parent = _Node(1, "foo")
        child = _Node(2, "bar", parent)
        parent._left_child = child

        # When
        got = child.get_parent()

        # Then
        self.assertEqual(got, parent)

    def test_get_value(self):
        # Given
        node = _Node(1, "foo")

        # When
        value = node.get_value()

        # Then
        self.assertEqual(value, "foo")

    def test_get_key(self):
        # Given
        node = _Node(1, "foo")

        # When
        key = node.get_key()

        # Then
        self.assertEqual(key, 1)


#-------------------------------------------------------------------#

class TestBST(unittest.TestCase):

#-------------------------------------------------------------------#

    def test_create(self):
        # Given / When
        bts = BST()

        # Then
        self.assertEqual(bts._root_node, None)

#-------------------------------------------------------------------#

    def test_insert_root(self):
        # Given
        bst = BST()

        # When
        bst.insert(1, "foo")

        # Then
        self.assertEqual(bst._root_node._value, "foo")

    def test_insert_bad_key(self):
        # Given
        bst = BST()

        # When
        with self.assertRaises(Exception) as ex:
            bst.insert("foo", "bar")

        # Then
        self.assertEqual(str(ex.exception), "Key must be number!")

    def test_insert_nothing_given(self):
        # Given
        bst = BST()

        # When
        with self.assertRaises(Exception) as ex:
            bst.insert()

        # Then
        self.assertEqual(str(ex.exception), "Nothing to insert!")

    def test_insert_smaller(self):
        # Given
        bst = BST()
        bst.insert(5, "foo")

        # When
        bst.insert(4, "bar")

        # Then
        self.assertEqual(bst._root_node._value, "foo")
        self.assertEqual(bst._root_node.get_left_child()._value, "bar")

    def test_insert_larger(self):
        # Given
        bst = BST()
        bst.insert(5, "foo")

        # When
        bst.insert(6, "bar")

        # Then
        self.assertEqual(bst._root_node._value, "foo")
        self.assertEqual(bst._root_node.get_right_child()._value, "bar")

    def test_insert_same_value(self):
        # Given
        bst = BST()
        bst.insert(5, "foo")

        # When
        with self.assertRaises(Exception) as ex:
            bst.insert(5, "bar")

        # Then
        self.assertEqual(str(ex.exception), "Key is already in BST!")

#-------------------------------------------------------------------#

        # Then
        self.assertEqual(str(ex.exception), "Value is already in BST!")


if __name__ == "__main__":
    unittest.main()