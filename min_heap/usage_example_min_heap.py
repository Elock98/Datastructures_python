from min_heap import MinHeap

heap = MinHeap()

heap.add(3)
heap.print_heap()
heap.add(99)
heap.print_heap()
heap.add(4)
heap.print_heap()
heap.add(1122)
heap.print_heap()
heap.add(2)
heap.print_heap()
heap.add(9873)
heap.print_heap()
heap.add(2342)
heap.print_heap()
heap.add(1)
heap.print_heap()
heap.add(0)
heap.print_heap()
print(heap.pop_index(4))
heap.print_heap()
print(heap.pop_value(3))
heap.print_heap()
print(heap.pop_index(0))
heap.print_heap()