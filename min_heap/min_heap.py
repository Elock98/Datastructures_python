from numbers import Number
import math

class MinHeap:

    def __init__(self) -> None:
        self._elements = []

    def add(self, element=None) -> None:
        '''Add value to the heap'''
        assert element != None, f"No element given!"
        assert isinstance(element, Number), f"No number element given!"
        self._elements.append(element)
        self._bubble_up() # Sort

    def _check_index(self, index:int="NoIndex") -> None:
        '''Check the validity of given index'''
        assert index != "NoIndex", f"No index given!"
        assert isinstance(index, int), f"Index needs to be int type!"
        assert index > -1 and index < len(self._elements), f"Index out of heap range!"

    def _get_left_child_index(self, index:int="NoIndex") -> int:
        '''Returns the index of the left child'''
        self._check_index(index)
        return index*2+1

    def _get_right_child_index(self, index:int="NoIndex") -> int:
        '''Returns the index of the right child'''
        self._check_index(index)
        return index*2+2

    def get_value(self, index:int="NoIndex") -> None:
        '''Returns the value stored at index'''
        self._check_index(index) # If correct index given
        return self._elements[index]

    def _is_right_child(self, index:int="NoIndex") -> bool:
        '''Returns false if the given index is a right child'''
        self._check_index(index)
        if index % 2:
            return False
        return True

    def _is_left_child(self, index:int="NoIndex") -> bool:
        '''Returns false if the given index is a left child'''
        self._check_index(index)
        if index % 2:
            return True
        return False

    def _get_parent_index(self, index:int="NoIndex") -> int:
        '''Returns the index of parent'''
        self._check_index(index)
        assert index != 0, f"Root element has no parent!"

        if self._is_left_child(index):
            return math.floor((index-1)/2)

        if self._is_right_child(index):
            return math.floor((index-2)/2)

    def _swap_elements(self, index_1:int="NoIndex", 
                            index_2:int="NoIndex") -> None:
        '''Swaps two elements places in the heap'''
        assert index_1 != "NoIndex" and index_2 != "NoIndex", f"Missing index!"
        self._check_index(index_1)
        self._check_index(index_2)

        temp = self.get_value(index_1)
        self._elements[index_1] = self.get_value(index_2)
        self._elements[index_2] = temp

    def _bubble_up(self, index:int=None) -> None:
        '''Moves element upwards in the heap until sorted'''
        assert len(self._elements) != 0, f"No elements in heap!"

        if len(self._elements) == 1:
            return
        
        if index == None: # Set index to last in heap
            inserted_index = len(self._elements)-1
        else:
            inserted_index = index
        
        try:
            parent_index = self._get_parent_index(inserted_index)
        except Exception as e:
            if str(e) == "Root element has no parent!":
                '''If element is root element, bubble up 
                   is no longer possible.'''
                return
            raise e

        # If parent is larger, bubble up
        if self.get_value(inserted_index) < self.get_value(parent_index):
            self._swap_elements(inserted_index, parent_index)
            self._bubble_up(parent_index)

    def _bubble_down(self, index:int=None) -> None:
        '''Moves element downwards in the heap until sorted'''
        assert index != None, f"No index given!"
        assert len(self._elements) != 0, f"No elements in heap!"
        
        self._check_index(index)
        
        if len(self._elements) == 1:
            return
        
        removed_index = index
        replaced_value = self.get_value(removed_index)

        # Root element
        try:
            parent_index = self._get_parent_index(removed_index)
        except Exception as e:
            if str(e) != "Root element has no parent!":      
                if replaced_value < self.get_value(parent_index):
                    self._swap_elements(removed_index, parent_index)
                    self._bubble_up(parent_index)
                    return

        left_child_index = self._get_left_child_index(removed_index)
        right_child_index = self._get_right_child_index(removed_index)

        # Check left child
        try:
            left_child_value = self.get_value(left_child_index)
        except Exception as e:
            if str(e) == "Index out of heap range!":
                return

        # Check right child
        try:
            right_child = True
            right_child_value = self.get_value(right_child_index)
        except Exception as e:
            if str(e) == "Index out of heap range!":
                right_child = False
        
        if right_child == False and left_child_value > replaced_value:
            return

        if replaced_value < left_child_value and\
            replaced_value < right_child_value:
            return

        if left_child_value < right_child_value:
            if left_child_index < len(self._elements):
                self._swap_elements(removed_index, left_child_index)
                self._bubble_down(left_child_index)
        else:
            if right_child_index < len(self._elements):
                self._swap_elements(removed_index, right_child_index)
                self._bubble_down(right_child_index)

    def print_heap(self) -> None:
        '''Prints the heap as a list'''
        print(self._elements)

    def _get_index_by_value(self, value:int=None) -> int:
        '''Returns the index of a given value'''
        assert value != None, f"No value given!"
        assert isinstance(value, Number), f"Bad value given!"

        for index, element in enumerate(self._elements):
            if value == element:
                return index
        
        raise ValueError(f"Value not in heap!")

    def pop_value(self, value:int=None) -> int:
        '''Removes a given value from the heap
           and returns it.'''
        return self.pop_index(self._get_index_by_value(value))

    def pop_index(self, index:int=None) -> int:
        '''Removes a given index from the heap
            and returns it.'''
        try:
            self._check_index(index)
        except Exception as e:
            if str(e) == "Root element has no parent!" and\
                len(self._elements) == 1:
                value = self._elements[0]
                self._elements = []
                return value
            raise e

        if index == len(self._elements)-1:
            value = self._elements[-1]
            self._elements = self._elements[:-1]
            return value

        value = self._elements[index]
        self._swap_elements(index, len(self._elements)-1)
        self._elements = self._elements[:-1]
        self._bubble_down(index)
        return value
