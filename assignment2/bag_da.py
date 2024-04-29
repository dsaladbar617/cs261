# Name: Daniel Salazar
# OSU Email: salazdan@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date: Apr 29, 2024
# Description: Implementing a bag class


from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        This method adds a new value to the bag
        """
        # if self._da.get_capacity() == self._da.length():
        self._da.append(value)

        return

    def remove(self, value: object) -> bool:
        """
        This method removes the first instance of the value from the bag
        """
        removed = False
        for i in range(self._da.length()):
            if value == self._da.get_at_index(i):
                self._da.remove_at_index(i)
                removed = True
                break
        return removed

    def count(self, value: object) -> int:
        """
        This method counts the number of times the value appears in the bag
        """
        count = 0

        for i in range(self._da.length()):
            if value == self._da.get_at_index(i):
                count += 1
        return count

    def clear(self) -> None:
        """
        This method clears the bag of all values
        """
        self._da = DynamicArray()
        return

    def equal(self, second_bag: "Bag") -> bool:
        """
        This method checks if two bags are equal
        """
        match = False
        match_elements = self._da.length()
        second_match_elements = second_bag._da.length()
        if self._da.length() == 0 and second_bag.size() == 0:
            match = True

        if self._da.length() != second_bag._da.length():
            return match

        for i in range(self._da.length()):
            current_match = False
            for j in range(second_bag.size()):
                if self._da.get_at_index(i) == second_bag._da.get_at_index(j):
                    match_elements -= 1
                    current_match = True
                if second_bag._da.get_at_index(i) == self._da.get_at_index(j):
                   second_match_elements -= 1
                   current_match = True

                if j == second_bag._da.length() - 1 and current_match == False:
                    match = False
                    break

                if match_elements == 0 and second_match_elements == 0:
                    match = True
            else:
                continue

            break

        return match

    def __iter__(self):
        """
        This method returns an iterator object
        """

        self._index = 0

        return self

    def __next__(self):
        """
        This method returns the next value in the bag
        """
        try:
            value = self._da[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1

        return value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
