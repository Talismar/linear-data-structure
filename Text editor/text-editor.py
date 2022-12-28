import keyboard

class No:
  def __init__(self, value):
    self.prev = None
    self.value = value
    self.next = None

class LinkedList:
  
  def __init__(self):
    self.head = None
    self.tail = None
    self.cursor = None

  def insertBegin(self, value):
    # print("InsertBegin")
    no = No(value)
    
    if self.head == None:
      self.tail = no
      self.head = no 
      self.cursor = no
      return
    
    self.head.prev = no
    no.next = self.head
    self.head = no
    self.cursor = no

  def insertEnd(self, value):
    no = No(value)

    if self.tail == None:
      self.head = no
      self.tail = no
    
    else:
      self.tail.next = no
      no.prev = self.tail
      self.tail = no
      
    self.cursor = no

  def print_cursor(self,):
    current = self.cursor
    text = ""

    while current != None:
      text +=  current.value
      current = current.prev

    current = self.tail
    new_text = ""

    while current != None:
      if current != self.cursor:
        new_text += current.value
        current = current.prev

      else:
        break
    
    return text[::-1] + "_" + new_text[::-1]

  def removeEnd(self):
    if self.tail != None:
      
      self.tail = self.tail.prev
      self.cursor = self.cursor.prev

      try:
        self.tail.next = None
        self.cursor.next = None
      except AttributeError: # NoneType Error
        self.tail = None
        self.head = None
        self.cursor = None

  def removeCursor(self):
    """ Para remover se o cursor estiver no final """
    try:
      if self.cursor.next == None:
        self.removeEnd()
        return
    except AttributeError:
      print("Attribute Error in function removeCursor")
      return

      
    aux = self.tail
    while aux != None:
      if aux == self.cursor:
        aux = self.cursor.next
        aux.prev = self.cursor.prev
        break

      aux = aux.prev
    
    try:
      self.cursor.prev.next = self.cursor.next
      self.cursor.next.prev =  self.cursor.prev
      self.cursor = self.cursor.prev
    except AttributeError:
      """ Remover quando o cursor está no inicio da lista|| remover do head """

      self.cursor = None
      self.head = self.head.next

      print("Attribure Error prev")

  def insertCursor(self, value):

    if self.tail == None:
      self.insertEnd(value)
    
    elif self.cursor == None:
      self.insertBegin(value)

    elif self.cursor.next == None:
      self.insertEnd(value)

    else:
      # inserindo em qualquer lugar que não seja no final e na cabeça
      no = No(value)
      
      no.next = self.cursor.next # None
      no.prev = self.cursor # No prev
      
      self.cursor.next.prev = no
      self.cursor.next = no # [[None, T, None], a, None]
      
      self.cursor = no
      
  def moveCursor(self, action):
    
    if self.cursor != None:
      
      match action:
        case 'left':
          if self.cursor.prev != None:
            self.cursor = self.cursor.prev       
          else:
            self.cursor = None

        case 'right':
          if self.cursor.next != None:
            self.cursor = self.cursor.next

    else:
      if action == 'right':
        self.cursor = self.head

l = LinkedList()

key_shift = ""
accents = ""

while True:

  # Wait for the next event.
  event = keyboard.read_event()

  if event.event_type == keyboard.KEY_DOWN:
    
    if key_shift != "":
      # Não adicionar a palavra SHIFT em Maiúsculo
      if event.name != key_shift:
        l.insertCursor(event.name.upper())

      key_shift = ""
    
    elif accents != "":
      l.insertCursor(insert_a.insert_accented(event.name, accents))
      accents = ""

    else:
      match event.name:
        case 'shift':
          key_shift = event.name

        case 'space':
          l.insertCursor(" ")

        case 'up' | 'down' | 'ctrl' | 'alt':
          pass

        case 'left' | 'right':
          l.moveCursor(event.name)
      
        case 'enter':
          l.insertCursor('\n')

        case '´' | '`' | '^' | '~':
          accents = event.name
        
        case 'backspace':
          l.removeCursor()

        case _:
          l.insertCursor(event.name)

    print("*"*50)
    print(l.print_cursor())