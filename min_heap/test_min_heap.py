import io
import unittest

from unittest.mock import patch
from min_heap import MinHeap


class TestMinHeap(unittest.TestCase):

    @patch("min_heap.MinHeap._bubble_up")
    def test_add_int(self, mock__bubble_up):
        # Given
        heap = MinHeap()
        element = 10

        # When
        heap.add(element)

        # Then
        self.assertEqual(heap._elements, [element])
        mock__bubble_up.assert_called_once()

    @patch("min_heap.MinHeap._bubble_up")
    def test_add_float(self, mock__bubble_up):
        # Given
        heap = MinHeap()
        element = 13.37

        # When
        heap.add(element)

        # Then
        self.assertEqual(heap._elements, [element])
        self.assertEqual(len(heap._elements), 1)
        mock__bubble_up.assert_called_once()

    @patch("min_heap.MinHeap._bubble_up")
    def test_add_str(self, mock__bubble_up):
        # Given
        heap = MinHeap()
        element = "13.37"

        # When
        with self.assertRaises(Exception) as ex:
            heap.add(element)

        # Then
        self.assertNotEqual(heap._elements, [element])
        self.assertEqual(heap._elements, [])
        self.assertEqual(str(ex.exception), f"No number element given!")
        mock__bubble_up.assert_not_called()

    @patch("min_heap.MinHeap._bubble_up")
    def test_add_no_element(self, mock__bubble_up):
        # Given
        heap = MinHeap()

        # When
        with self.assertRaises(Exception) as ex:
            heap.add()

        # Then
        self.assertEqual(heap._elements, [])
        self.assertEqual(str(ex.exception), f"No element given!")
        mock__bubble_up.assert_not_called()

#-------------------------------------------------------------------#

    def test__check_index_no_index(self):
        # Given
        heap = MinHeap()

        # When
        with self.assertRaises(Exception) as ex:
            heap._check_index()
        
        # Then
        self.assertEqual(str(ex.exception), f"No index given!")
    
    def test__check_index_bad_index(self):
        # Given
        heap = MinHeap()

        # When
        with self.assertRaises(Exception) as ex:
            heap._check_index("foo")
        
        # Then
        self.assertEqual(str(ex.exception), f"Index needs to be int type!")

    def test__check_index_out_of_range_low(self):
        # Given
        heap = MinHeap()
        heap._elements = [1, 2, 3, 4, 5]
        # When
        with self.assertRaises(Exception) as ex:
            heap._check_index(-1)
        
        # Then
        self.assertEqual(str(ex.exception), f"Index out of heap range!")

    def test__check_index_out_of_range_high(self):
        # Given
        heap = MinHeap()
        heap._elements = [1, 2, 3, 4, 5]
        # When
        with self.assertRaises(Exception) as ex:
            heap._check_index(25)
        
        # Then
        self.assertEqual(str(ex.exception), f"Index out of heap range!")

    def test__check_index(self):
        # Given
        heap = MinHeap()
        heap._elements = [1, 2, 3, 4]

        # When
        heap._check_index(2)

#-------------------------------------------------------------------#

    @patch("min_heap.MinHeap._check_index")
    def test__get_left_child_index(self, mock__check_index):
        # Given
        heap = MinHeap()
        heap._elements = [1, 2, 3, 4, 5]

        # When
        index = heap._get_left_child_index(0)

        # Then
        mock__check_index.assert_called_once()
        self.assertEqual(index, 1)
    
    @patch("min_heap.MinHeap._check_index")
    def test__get_right_child_index(self, mock__check_index):
        # Given
        heap = MinHeap()
        heap._elements = [1, 2, 3, 4, 5]

        # When
        index = heap._get_right_child_index(0)

        # Then
        mock__check_index.assert_called_once()
        self.assertEqual(index, 2)

#-------------------------------------------------------------------#

    @patch("min_heap.MinHeap._check_index")
    def test_get_value(self, mock__check_index):
        # Given
        heap = MinHeap()
        heap._elements = [1, 2, 3, 4, 5]

        # When
        value = heap.get_value(3)

        # Then
        mock__check_index.assert_called_once()
        self.assertEqual(value, 4)

#-------------------------------------------------------------------#

    @patch("min_heap.MinHeap._check_index")
    def test__is_left_child_TRUE(self, mock__check_index):
        # Given
        heap = MinHeap()
        heap._elements = [1, 2, 3, 4, 5]

        # When
        is_left = heap._is_left_child(3)

        # Then
        mock__check_index.assert_called_once()
        self.assertEqual(is_left, True)

    @patch("min_heap.MinHeap._check_index")
    def test__is_left_child_FALSE(self, mock__check_index):
        # Given
        heap = MinHeap()
        heap._elements = [1, 2, 3, 4, 5]

        # When
        is_left = heap._is_left_child(4)

        # Then
        mock__check_index.assert_called_once()
        self.assertEqual(is_left, False)

    @patch("min_heap.MinHeap._check_index")
    def test__is_right_child_TRUE(self, mock__check_index):
        # Given
        heap = MinHeap()
        heap._elements = [1, 2, 3, 4, 5]

        # When
        is_left = heap._is_right_child(4)

        # Then
        mock__check_index.assert_called_once()
        self.assertEqual(is_left, True)

    @patch("min_heap.MinHeap._check_index")
    def test__is_right_child_FALSE(self, mock__check_index):
        # Given
        heap = MinHeap()
        heap._elements = [1, 2, 3, 4, 5]

        # When
        is_left = heap._is_right_child(3)

        # Then
        mock__check_index.assert_called_once()
        self.assertEqual(is_left, False)

#-------------------------------------------------------------------#

    @patch("min_heap.MinHeap._check_index")
    def test__get_parent_index_root(self, mock__check_index):
        # Given
        heap = MinHeap()
        heap._elements = [1, 2, 3, 4, 5]

        # When
        with self.assertRaises(Exception) as ex:
            heap._get_parent_index(0)
        
        # Then
        mock__check_index.assert_called_once()
        self.assertEqual(str(ex.exception), f"Root element has no parent!")

    @patch("min_heap.MinHeap._check_index")
    def test__get_parent_index_bad_index(self, mock__check_index):
        # Given
        heap = MinHeap()
        heap._elements = [1, 2, 3, 4, 5]
        mock__check_index.side_effect = Exception(f"Index needs to be int type!")

        # When
        with self.assertRaises(Exception) as ex:
            heap._get_parent_index("foo")
        
        # Then
        mock__check_index.assert_called()
        self.assertEqual(str(ex.exception), f"Index needs to be int type!")

    @patch("min_heap.MinHeap._is_right_child")
    @patch("min_heap.MinHeap._is_left_child")
    @patch("min_heap.MinHeap._check_index")
    def test__get_parent_index_left(self, mock__check_index,
                                mock__is_left_child,
                                mock__is_right_child):
        # Given
        heap = MinHeap()
        heap._elements = [1, 2, 3, 4, 5]
        mock__is_left_child.return_value = True
        mock__is_right_child.return_value = False
        
        # When
        index = heap._get_parent_index(3)

        # Then
        mock__check_index.assert_called_once()
        mock__is_left_child.assert_called_once()
        mock__is_right_child.assert_not_called()
        self.assertEqual(index, 1)

    @patch("min_heap.MinHeap._is_right_child")
    @patch("min_heap.MinHeap._is_left_child")
    @patch("min_heap.MinHeap._check_index")
    def test__get_parent_index_right(self, mock__check_index,
                                mock__is_left_child,
                                mock__is_right_child):
        # Given
        heap = MinHeap()
        heap._elements = [1, 2, 3, 4, 5]
        mock__is_left_child.return_value = False
        mock__is_right_child.return_value = True

        # When
        index = heap._get_parent_index(4)

        # Then
        mock__check_index.assert_called_once()
        mock__is_left_child.assert_called_once()
        mock__is_right_child.assert_called_once()
        self.assertEqual(index, 1)

#-------------------------------------------------------------------#

    def test__swap_elements(self):
        # Given
        heap = MinHeap()
        heap._elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # When
        heap._swap_elements(0, 9)

        # Then
        self.assertEqual(heap._elements, [9, 1, 2, 3, 4, 5, 6, 7, 8, 0])

    def test__swap_elements_no_index(self):
        # Given
        heap = MinHeap()
        heap._elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # When
        with self.assertRaises(Exception) as ex:
            heap._swap_elements()

        # Then
        self.assertEqual(str(ex.exception), f"Missing index!")

    def test__swap_elements_one_index(self):
        # Given
        heap = MinHeap()
        heap._elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # When
        with self.assertRaises(Exception) as ex:
            heap._swap_elements(5)

        # Then
        self.assertEqual(str(ex.exception), f"Missing index!")
    
    def test__swap_elements_bad_index(self):
        # Given
        heap = MinHeap()
        heap._elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # When
        with self.assertRaises(Exception) as ex:
            heap._swap_elements("foo", "bar")

        # Then
        self.assertEqual(str(ex.exception), f"Index needs to be int type!")

#-------------------------------------------------------------------#

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_heap(self, mock_stdout):
        # Given
        heap = MinHeap()
        heap._elements = [1, 2, 3, 4, 5, 6]

        # When
        heap.print_heap()

        # Then
        self.assertEqual(mock_stdout.getvalue(), "[1, 2, 3, 4, 5, 6]\n")

#-------------------------------------------------------------------#

    def test__get_index_by_value(self):
        # Given
        heap = MinHeap()
        heap._elements = [0, 12, 32, 555, 1, 345345]

        # When
        index = heap._get_index_by_value(555)

        # Then
        self.assertEqual(index, 3)

    def test__get_index_by_value_not_in_heap(self):
        # Given
        heap = MinHeap()
        heap._elements = [0, 12, 32, 555, 1, 345345]

        # When
        with self.assertRaises(Exception) as ex:
            heap._get_index_by_value(4321)

        # Then
        self.assertEqual(str(ex.exception), f"Value not in heap!")

    def test__get_index_by_value_no_value(self):
        # Given
        heap = MinHeap()
        heap._elements = [0, 12, 32, 555, 1, 345345]

        # When
        with self.assertRaises(Exception) as ex:
            heap._get_index_by_value()

        # Then
        self.assertEqual(str(ex.exception), f"No value given!")

    def test__get_index_by_value_bad_value(self):
        # Given
        heap = MinHeap()
        heap._elements = [0, 12, 32, 555, 1, 345345]

        # When
        with self.assertRaises(Exception) as ex:
            heap._get_index_by_value("foo")

        # Then
        self.assertEqual(str(ex.exception), f"Bad value given!")

#-------------------------------------------------------------------#

    def test__bubble_up_root(self):
        # Given
        heap = MinHeap()
        heap._elements = [1]

        # When
        heap._bubble_up()

        # Then
        self.assertEqual(heap._elements, [1])

    def test__bubble_up(self):
        # Given
        heap = MinHeap()
        heap._elements = [0, 1, 2, 3, 55, 6, 7, 8, 9]
        heap._elements.append(5)

        # When
        heap._bubble_up()

        # Then
        self.assertEqual(heap._elements, [0, 1, 2, 3, 5, 6, 7, 8, 9, 55])

    def test__bubble_up_no_elements(self):
        # Given
        heap = MinHeap()

        # When
        with self.assertRaises(Exception) as ex:
            heap._bubble_up()

        # Then
        self.assertEqual(str(ex.exception), "No elements in heap!")

#-------------------------------------------------------------------#

    def test__bubble_down(self):
        # Given
        heap = MinHeap()
        heap._elements = [0, 100, 8, 14, 22, 30]

        # When
        heap._bubble_down(1)

        # Then
        self.assertEqual(heap._elements, [0, 14, 8, 100, 22, 30])

    def test__bubble_down_last_element(self):
        # Given
        heap = MinHeap()
        heap._elements = [0, 14, 8, 100, 22, 30]

        # When
        heap._bubble_down(len(heap._elements)-1) # Last element removed

        # Then
        self.assertEqual(heap._elements, [0, 14, 8, 100, 22, 30])

    def test__bubble_down_no_elements(self):
        # Given
        heap = MinHeap()
        
        # When
        with self.assertRaises(Exception) as ex:
            heap._bubble_down(4)

        # Then
        self.assertEqual(str(ex.exception), "No elements in heap!")

    def test__bubble_down_no_index_given(self):
        # Given
        heap = MinHeap()
        
        # When
        with self.assertRaises(Exception) as ex:
            heap._bubble_down()

        # Then
        self.assertEqual(str(ex.exception), "No index given!")
    
#-------------------------------------------------------------------#

    def test_pop_index(self):
        # Given
        heap = MinHeap()
        heap._elements = [0, 1, 4, 2, 99, 9873, 2342, 1122, 3]

        # When
        heap.pop_index(4)

        # Then
        self.assertEqual(heap._elements, [0, 1, 4, 2, 3, 9873, 2342, 1122])

    def test_pop_value(self):
        # Given
        heap = MinHeap()
        heap._elements = [0, 1, 4, 2, 99, 9873, 2342, 1122, 3]

        # When
        heap.pop_value(99)

        # Then
        self.assertEqual(heap._elements, [0, 1, 4, 2, 3, 9873, 2342, 1122])

#-------------------------------------------------------------------#


if __name__ == "__main__":
    unittest.main()