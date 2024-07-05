class Linked_List:
    
    class __Node:
        
        def __init__(self, val):
            # Declare and initialize the public attributes for objects of the
            # Node class. TODO replace pass with your implementation
            self.previous=None
            self.value=val
            self.next=None

    def __init__(self):
        # Declare and initialize the private attributes for objects of the
        # sentineled Linked_List class TODO replace pass with your
        # implementation
        self.__header=Linked_List.__Node(None)
        self.__trailer=Linked_List.__Node(None)
        self.__header.next=self.__trailer
        self.__trailer.previous=self.__header
        self.__size=0

    def __len__(self):
        # Return the number of value-containing nodes in this list. TODO replace
        # pass with your implementation
        return self.__size

    def append_element(self, val):
        # Increase the size of the list by one, and add a node containing val at
        # the new tail position. this is the only way to add items at the tail
        # position. TODO replace pass with your implementation
        newest=Linked_List.__Node(val)
        newest.previous=self.__trailer.previous
        newest.next=self.__trailer
        self.__trailer.previous.next=newest
        self.__trailer.previous=newest
        self.__size=self.__size+1

        # Optimized current walk function. It starts at the nearest endpoint depending on the value of the index which makes it faster.

    def __current_walk(self, index):
        if index<=self.__size//2:
            current=self.__header
            for i in range(index+1):
                current=current.next
            return current

        elif index>=self.__size//2:
            current=self.__trailer
            #for i in range(self.__size//2,self.__size-1):
            for i in range(index-1,self.__size-1):
                current=current.previous
            return current

        elif index==self.size:
            current=self.__trailer.previous
            return current

    # Old current walk function - not optimized
    # def __current_walk(self, index):
    #     current=self.__header
    #     for i in range(index+1):
    #          current=current.next
    #     return current
    

    def insert_element_at(self, val, index):
        # Assuming the head position (not the header node) is indexed 0, add a
        # node containing val at the specified index. If the index is not a
        # valid position within the list, raise an IndexError exception. This
        # method cannot be used to add an item at the tail position. TODO
        # replace pass with your implementation
        
        if index<0:
            raise IndexError
        elif index == self.__size:
            raise IndexError
        elif index>self.__size:
            raise IndexError
        else:
            newest=Linked_List.__Node(val)
            current=self.__current_walk(index)

            newest.next=current
            newest.previous=current.previous
            current.previous.next = newest
            current.previous=newest

            self.__size=self.__size+1

    def remove_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, remove
        # and return the value stored in the node at the specified index. If the
        # index is invalid, raise an IndexError exception. TODO replace pass
        # with your implementation

        if index<0:
            raise IndexError
        elif index == self.__size:
            raise IndexError
        elif index>self.__size:
            raise IndexError
        else:
            current=self.__current_walk(index)

            current.previous.next=current.next
            current.next.previous=current.previous
            self.__size=self.__size-1
            value=current.value
            current.previous=None
            current.value=None
            current.next=None

        return value

    def get_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, return
        # the value stored in the node at the specified index, but do not unlink
        # it from the list. If the specified index is invalid, raise an
        # IndexError exception. TODO replace pass with your implementation
        if index<0:
            raise IndexError
        elif index == self.__size:
            raise IndexError
        elif index>self.__size:
            raise IndexError
        else:
            current=self.__current_walk(index)
            value=current.value
            return value


    def rotate_left(self):
        # Rotate the list left one position. Conceptual indices should all
        # decrease by one, except for the head, which should become the tail.
        # For example, if the list is [ 5, 7, 9, -4 ], this method should alter
        # it to [ 7, 9, -4, 5 ]. This method should modify the list in place and
        # must not return a value. TODO replace pass with your implementation.
        if self.__size>0:
            value=self.__header.next.value
            self.remove_element_at(0)
            self.append_element(value)
        
        
    def __str__(self):
        # Return a string representation of the list's contents. An empty list
        # should appear as [ ]. A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ]. You may assume
        # that the values stored inside of the node objects implement the
        # __str__() method, so you call str(val_object) on them to get their
        # string representations. TODO replace pass with your implementation
        
        current = self.__header.next
        string=""

        if self.__size==0:
            return "[ ]"
        elif self.__size==1:
            return "[ "+str(current.value)+" ]"
        elif self.__size>1:
            while current != self.__trailer:
                string=string+str(current.value)+", "
                current=current.next

            new_string=string[:-1]
            newer_string=new_string[:-1]
            newest_string="[ "+newer_string+" ]"
            return newest_string

    def __iter__(self):
        # Initialize a new attribute for walking through your list TODO insert
        # your initialization code before the return statement. Do not modify
        # the return statement.
        self.para=self.__header
        return self

    def __next__(self):
        # Using the attribute that you initialized in __iter__(), fetch the next
        # value and return it. If there are no more values to fetch, raise a
        # StopIteration exception. TODO replace pass with your implementation
        if self.para == self.__trailer.previous:
            raise StopIteration
        self.para= self.para.next
        return self.para.value
        

    def __reversed__(self):
        # Construct and return a new Linked_List object whose nodes alias the
        # same objects as the nodes in this list, but in reverse order. For a
        # Linked_List object ll, Python will automatically call this function
        # when it encounters a call to reversed(ll) in an application. If
        # print(ll) displays [ 1, 2, 3, 4, 5 ], then print(reversed(ll)) should
        # display [ 5, 4, 3, 2, 1 ]. This method does not change the state of
        # the object on which it is called. Calling print(ll) again will still
        # display [ 1, 2, 3, 4, 5 ], even after calling reversed(ll). This
        # method must operate in linear time.

        if self.__size==0:
            return Linked_List()
        else:
            Reversed_linked_list=Linked_List()
            current=self.__trailer.previous
            while current.previous != self.__header:
                Reversed_linked_list.append_element(current.value)
                current=current.previous
            Reversed_linked_list.append_element(self.__header.next.value)
            return Reversed_linked_list


if __name__ == '__main__':
    # Your test code should go here. Be sure to look at cases when the list is
    # empty, when it has one element, and when it has several elements. Do the
    # indexed methods raise exceptions when given invalid indices? Do they
    # position items correctly when given valid indices? Does the string
    # representation of your list conform to the specified format? Does removing
    # an element function correctly regardless of that element's location? Does
    # a for loop iterate through your list from head to tail? Does a for loop
    # iterate through your reversed list from tail to head? Your writeup should
    # explain why you chose the test cases. Leave all test cases in your code
    # when submitting. TODO replace pass with your tests

    #Tests for __len__(self)
    x = Linked_List()
    print(len(x),"This should be 0")
    x.append_element(0)
    print(len(x),"This should be 1")
    x.append_element(1)
    x.append_element(2)
    x.append_element(3)
    x.append_element(4)
    print(len(x),"This should be 5")

    #Tests for append_element(self, val)
    l=Linked_List()
    l.append_element("Data")
    print(l,"This should be [ Data ]")
    print(len(l), "This should be 1")

    #Tests for insert_element_at(self, val, index):
    #Recall that x is a linked list with five nodes containing the values from 0 to 4.
    x.insert_element_at(100,2)
    print(x, "This should be [ 0, 1, 100, 2, 3, 4 ]")
    print(len(x), "This should be 6")

    try:
        x.insert_element_at(100,-3)
    except IndexError:
        print("Error, negative indexing is not allowed")

    try:
        x.insert_element_at(100,3)
    except IndexError:
        print("It raised an error that it never should have been raised")


    #Tests for remove_element_at(self, index):
    #Recall that x is a linked list with six nodes that looks like [ 0, 1, 100, 100, 2, 3, 4 ].
    print(x)
    x.remove_element_at(2)
    print(x, "This should be [ 0, 1, 100, 2, 3, 4 ]")
    print(len(x), "This should be 6")

    try:
        x.remove_element_at(-3)
    except IndexError:
        print("Error, negative indexing is not allowed")

    try:
        x.remove_element_at(2)
    except IndexError:
        print("It raised an error that it never should have been raised")
    
    #Tests for get_element_at(self, index):
    #Recall that x is a linked list that looks like [ 0, 1, 2, 3, 4 ].
    print(x.get_element_at(3), "This should be 3")
    
    try:
        x.get_element_at(-3)
    except IndexError:
        print("Error, negative indexing is not allowed")

    try:
        x.get_element_at(2)
    except IndexError:
        print("It raised an error that it never should have been raised")

    #Tests for rotate_left(self):
    #Recall that x is a linked list that looks like [ 0, 1, 2, 3, 4 ].
    print(x, "This should be [ 0, 1, 2, 3, 4 ]")

    y=x.rotate_left()
    print(y, "This give None")

    #Tests for __str__(self):

    #Been doing this all along when printing linked lists. Does not need more.

    #Tests for __iter__(self): and __next__(self):
    for val in x:
        print(val, "Should return 1-2-3-4-0 (it ends with 0 because of the rotate left so this also checks the rotate left)")

    #Tests for __reversed__(self):
    t = Linked_List()
    t.append_element(0)
    t.append_element(1)
    t.append_element(2)
    t.append_element(3)
    t.append_element(4)
    print(t, "Should be [ 0, 1, 2, 3, 4 ]")
    print(t.__reversed__(), "Should be [ 4, 3, 2, 1, 0 ]")


    listlist = Linked_List()
    listlist.append_element(0)
    listlist.append_element(1)
    listlist.append_element(2)
    listlist.append_element(3)
    listlist.append_element(4)
    listlist.append_element(5)
    print(listlist.get_element_at(0))
    print(listlist.get_element_at(1))
    print(listlist.get_element_at(2))
    print(listlist.get_element_at(3))
    print(listlist.get_element_at(4))
    print(listlist.get_element_at(5))

