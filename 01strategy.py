"""
Strategy Design Pattern
=======================
It is a behavioral desing pattern, define multiple algorithms encapsulate them and make them interchangeable during runtime 
i.e means you can choose any of the algorithms without affecting client code.
"""


from abc import ABC, abstractmethod


class SortingStrategy(ABC):
    """Base sort strategy"""

    @abstractmethod
    def sort(self,arr):
        pass

# different sorting methods
class BubbleSort(SortingStrategy):
    """Define bubble sort algorithms here"""

    def sort(self,arr:list) -> list:
        arr.sort()
        return arr
    

class SelectionSort(SortingStrategy):
    """Define selection sort algorithms here"""

    def sort(self,arr:list) -> list:
        arr.sort()
        return arr
    

class Sorter:
    def __init__(self,sorting_strategy):
        self.sorting_strategy = sorting_strategy

    def get_sorted(self,arr):
        return self.sorting_strategy.sort(arr)
    
    
arr :list = [5,10,0,3,-2,-1]

# using bubble sort
print("using bubble sort")
bubble_sort = BubbleSort()
s1 :Sorter = Sorter(bubble_sort)
sorted_arr = s1.get_sorted(arr)
print(sorted_arr)

# using selection sort
print("using selection sort")
selection_sort = SelectionSort()
s2 :Sorter = Sorter(selection_sort)
sorted_arr2 = s2.get_sorted(arr)
print(sorted_arr2)



    

