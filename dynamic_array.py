"""
Dynamic Array
=============
Design a dynamic array class that supports the following operations:

- pushback(val)  — append val to the end
- popback()      — remove and return the last element (raise IndexError if empty)
- get(i)         — return element at index i (raise IndexError if out of bounds)
- set(i, val)    — set element at index i to val (raise IndexError if out of bounds)
- size()         — return the number of elements
- capacity()     — return the current allocated capacity

Implementation rules:
- Use a fixed-size list (e.g. [None] * capacity) as the underlying storage — no built-in list append
- Start with an initial capacity of 1
- When the array is full, double the capacity (resize + copy)
- When the array is less than 1/4 full after a pop, halve the capacity (but never go below 1)

Example usage:
    arr = DynamicArray()
    arr.pushback(1)   # [1]
    arr.pushback(2)   # [1, 2]
    arr.pushback(3)   # [1, 2, 3]
    arr.popback()     # returns 3, array is [1, 2]
    arr.get(0)        # returns 1
    arr.set(1, 9)     # array is [1, 9]
    arr.size()        # returns 2
    arr.capacity()    # returns 4 (doubled once, not yet shrunk)
"""


class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity

    # Get value at i-th index
    def get(self, i: int) -> int:
        return self.arr[i]

    # Set n at i-th index changes?
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    # Insert n in the last position of the array
    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        # insert at next empty position
        self.arr[self.length] = n
        self.length += 1

    # Remove the last element in the array
    def popback(self) -> int:
        if self.length > 0:
            # soft delete the last element
            self.length -= 1
        # return the popped element
        return self.arr[self.length]

    def resize(self) -> None:
        # Create new array of double capacity
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

        # Copy elements to new_arr
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity
