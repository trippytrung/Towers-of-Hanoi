from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    # TODO replace pass with any additional initializations you need.
    self.__front=0
    self.__back=0
    self.__size=0
    
  def __str__(self):
    # TODO replace pass with an implementation that returns a string of
    # exactly the same format as the __str__ method in the Linked_List_Deque.
    # Orient your string from front (left) to back (right).

    if self.__size==0:
        return "[ ]"
    elif self.__size==1:
        return "[ "+str(self.__contents[self.__front])+" ]"
    elif self.__size>1:
      stringy=""
      current = self.__front
      while current != self.__back:
        stringy=stringy+str(self.__contents[current])+", "
        current=(current+1+self.__capacity)%self.__capacity
      string=stringy+str(self.__contents[current])
      string = '[ ' + string + ' ]'
      return string
    
  def __len__(self):
    # TODO replace pass with an implementation that returns the number of
    # items in the deque. This method must run in constant time.
    return self.__size

  def __grow(self):
    # TODO replace pass with an implementation that doubles the capacity
    # and positions existing items in the deque starting in cell 0 (why is
    # necessary?)

    new_list=[]
    current=self.__front
    while current != self.__back:
      new_list.append(self.__contents[current])
      current = (current + 1) % self.__capacity
    new_list.append(self.__contents[self.__back])
    new_list += [None] * self.__capacity

    self.__front=0
    self.__back = self.__size-1
    self.__capacity *=2
    return new_list

    #Unfortunately, the following idea doesn't quite work...

    # moreSpace=[None]*self.__capacity
    # self.__contents+=moreSpace
    # self.__capacity*=2
    # cap_temp = self.__capacity//2
    # for i in range(0,cap_temp):
    #   self.__contents[(self.__front-i)%(cap_temp)]=self.__contents[cap_temp-i]
    # for i in range(0,cap_temp):
    #   self.__contents[cap_temp-i]=self.__contents[i]
    # #for i in range(cap_temp,self.__capacity+1):
    # for i in range(0,cap_temp):
    #   self.__contents[cap_temp-i]=None

  def push_front(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    
    if self.__size >= self.__capacity:
      self.__contents=self.__grow()
    self.__front=(self.__front-1+self.__capacity)%self.__capacity
    self.__contents[self.__front]=val
    self.__size+=1

  def pop_front(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if self.__size==0:
      return None
    else:
      value=self.__contents[self.__front]
      self.__front=(self.__front+1+self.__capacity)%self.__capacity
      self.__size-=1
      return value
    
  def peek_front(self):
    # TODO replace pass with your implementation.
    if self.__size==0:
      return None
    else:
      value=self.__contents[self.__front]
      return value
    
  def push_back(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.__size >=self.__capacity:
      self.__contents=self.__grow()
    self.__back= (self.__back+1+self.__capacity)%self.__capacity
    self.__contents[self.__back]=val 
    self.__size+=1
  
  def pop_back(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if self.__size==0:
      return None
    else:
      value=self.__contents[self.__back]
      self.__back=(self.__back-1+self.__capacity)%self.__capacity
      self.__size-=1
      return value

  def peek_back(self):
    # TODO replace pass with your implementation.
    if self.__size==0:
      return None
    else:
      value=self.__contents[self.__back]
      return value

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
