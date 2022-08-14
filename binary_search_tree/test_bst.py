import unittest

from bst import BST
from bst import _Node
from unittest.mock import patch

class TestNode(unittest.TestCase):

#-------------------------------------------------------------------#

    def test_create_root(self):
        # Given / When
        node = _Node()

        # Then
        self.assertEqual(node._left_child, None)
        self.assertEqual(node._right_child, None)
        self.assertEqual(node._parent, None)


    def test_create(self):
        # Given
        root_node = _Node()

        # When
        node = _Node(root_node)

        # Then
        self.assertEqual(node._left_child, None)
        self.assertEqual(node._right_child, None)
        self.assertEqual(node._parent, root_node)



class TestBST(unittest.TestCase):

    def test_create(self):
        pass


if __name__ == "__main__":
    unittest.main()