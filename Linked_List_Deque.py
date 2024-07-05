from Deque import Deque
from Linked_List import Linked_List

class Linked_List_Deque(Deque):

  def __init__(self):
    self.__list = Linked_List()

  def __str__(self):
    return str(self.__list)

  def __len__(self):
    return len(self.__list)
  
  # DO NOT CHANGE ANYTHING ABOVE THIS LINE
  
  def push_front(self, val):
    # TODO replace pass with your implementation.
    # Use the head position for the front.
    if len(self.__list)==0:
      self.__list.append_element(val)
    else:
      self.__list.insert_element_at(val, 0)
  
  def pop_front(self):
    # TODO replace pass with your implementation.
    # Use the head position for the front.
    if len(self.__list)==0:
      return None
    else:
      value=self.__list.remove_element_at(0)
      return value

  def peek_front(self):
    # TODO replace pass with your implementation.
    # Use the head position for the front.
    if len(self.__list)==0:
      return None
    else:
      value=self.__list.get_element_at(0)
      return value

  def push_back(self, val):
    # TODO replace pass with your implementation.
    # Use the tail position for the back.
    self.__list.append_element(val)
  
  def pop_back(self):
    # TODO replace pass with your implementation.
    # Use the tail position for the back.
    if len(self.__list)==0:
      return None
    else:
      value=self.__list.remove_element_at(self.__len__()-1)
      return value    

  def peek_back(self):
    # TODO replace pass with your implementation.
    # Use the tail position for the back.
    if len(self.__list)==0:
      return None
    else:
      value=self.__list.get_element_at(self.__len__()-1)
      return value

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
