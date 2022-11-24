from more-itertools import iter_except


# Defines a node in the singly linked list
class Node:

    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

# Defines the singly linked list
class LinkedList:
    def __init__(self, value=None):
        self._head = None # keep the head private. Not accessible outside this class
        self._tail = None
        self._current = None
        self._length = 0
        if value is not None:
            self.add_first(self, value)

    @getattr
    def __getattr__(self, current):
        return self._current


    def __iter__(self):
        def list_iterator(head):
            while head:
                yield head.val
                head = head.next
        return list_iterator(self._head)

    def __next__(self):
        yield self.current.next


    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: o(1)
    # Space Complexity: ?
    def get_first(self):
        return self._head.value


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def add_first(self, value):
        def do():
            self.current = Node(value)
            self._head, self._head.next = self.current, self._head
        try:
            for value in value:
                do()
        except TypeError as err:
            if 'int' in err:
                do()
            elif 'str' in err:
                for value in value.split():
                    do()
            else:
                raise
        finally:
            self._length += 1



    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: ?
    # Space Complexity: ?
    def search(self, value):
         for node in self:
             if node.value == value:
                 return True
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def __len__(self):
        return self._length

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: ?
    # Space Complexity: ?
    def get_at_index(self, index):
        pass

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: ?
    # Space Complexity: ?
    def get_last(self):
        pass

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def add_last(self, value):
        pass

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        pass

    # method to delete the first node found with specified value
    # Time Complexity: ?
    # Space Complexity: ?
    def delete(self, value):
        pass

    # method to print all the values in the linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def visit(self):
        helper_list = []
        current = self._head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: ?
    # Space Complexity: ?
    def reverse(self):
        pass
  
    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def find_middle_value(self):
        pass

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: ?
    # Space Complexity: ?
    def find_nth_from_end(self, n):
        pass

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: ?
    # Space Complexity: ?
    def has_cycle(self):
        pass

    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle(self):
        if self._head == None:
            return

        # navigate to last node
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = self._head # make the last node link to first node
