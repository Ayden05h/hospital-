class Patient:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        
    def __lt__(self, other):
        return self.priority < other.priority
    
    def __repr__(self):
        return f"{self.name}, {self.priority}"



class MinHeap:
    def __init__(self):
        self.heap = []
        
    def insert(self, patient):
        self.heap.append(patient)
        self._heapify_up(len(self.heap) - 1)

    # Remove and return the patient with highest priority
    def remove_min(self):
        if not self.heap:
            return None  # Edge case: empty heap
        if len(self.heap) == 1:
            return self.heap.pop()
        min_patient = self.heap[0]
        # Move last element to root and heapify down
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_patient

    # Peek at the patient with highest priority
    def peek(self):
        return self.heap[0] if self.heap else None

    # Heapify up after insertion
    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    # Heapify down after removal
    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def __repr__(self):
        return f"Heap: {self.heap}"




# Test your MinHeap class here including edge cases
heap = MinHeap()

heap.insert(Patient("Ayden", 13))
heap.insert(Patient("Bob", 67))
heap.insert(Patient("Dan", 41))
heap.insert(Patient("billy", 1))
heap.insert(Patient("chris", 7))

print("Heap after insertions:")
print(heap)

print("Peek at the highest priority patient:")
print(heap.peek())

print("removing the patients by priority:")
while heap.peek() is not None:
    print(heap.remove_min())
    
print("remove from empty:")
print(heap.remove_min())