from tkinter import *
from tkinter import messagebox

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

    # Remover da cabeça 
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
      # inserindo em qualquer lugar que não seja no tail e no head
      no = No(value)
      
      no.next = self.cursor.next # None
      no.prev = self.cursor # No prev
      
      self.cursor.next.prev = no
      self.cursor.next = no # [[None, T, None], a, None]
      
      self.cursor = no
      
  def moveCursor(self, action):
    
    if self.cursor != None:
      
      match action:
        case 'Left':
          if self.cursor.prev != None:
            self.cursor = self.cursor.prev       
          else:
            self.cursor = None

        case 'Right':
          if self.cursor.next != None:
            self.cursor = self.cursor.next

    else:
      if action == 'Right':
        self.cursor = self.head

  def printBegin(self):
    current = self.head
    text = ""

    while current != None:
      text +=  current.value
      current = current.next

    return text
  

l = LinkedList()

def functionEvent(event):
  global l

  # print(event)

  match event.keysym: 
    case 'BackSpace':
      l.removeCursor()

    case 'Up' | 'Down' | 'Control_R' | 'Delete' | 'Control_L' | 'Alt_L' | 'Shift_L':
      # print("Key", type( event.keysym))
      pass

    case 'Left' | 'Right':
      l.moveCursor(event.keysym)

    case _:
      l.insertCursor(event.char)

  label.config(text=l.print_cursor())

  print(l.print_cursor())

def uploadFile():  
  global l
  with open("./words.txt", 'r', encoding='utf-8') as bd: 

    [l.insertCursor(i) for i in bd.read()]
    label.config(text=l.print_cursor())

def cleanAll():
  label.config(text="_")

def saveFile():  
  global l
  with open("./words.txt", 'w', encoding='utf-8') as bd: 
    bd.write(l.printBegin())
    
  msg_box = messagebox.askyesno("ET", message="Deseja sair ?")
  
  if msg_box:
    window.destroy()

window = Tk()
window.geometry("500x500")
window.title("Text Editor - EDL")

"Criando menu"
barradeMenus = Menu(window)
menuOp = Menu(barradeMenus, tearoff=0)

"Criando os itens do meuContatos"
menuOp.add_command(label="Upload File", command=uploadFile)
menuOp.add_command(label="Clean All", command=cleanAll)
menuOp.add_command(label="Save File", command=saveFile)
menuOp.add_separator()
menuOp.add_command(label="Fechar", command=window.quit)
barradeMenus.add_cascade(label="Opções", menu=menuOp)
"Adicionar o menu"
window.config(menu=barradeMenus)

window.bind('<Key>', functionEvent)

label = Label(window, anchor='nw', text="_", font=("Fira Code", 16), background='#96e637', wraplength=480, relief=RAISED)
label.place(x=10, y=10, width=480, height=480)

window.mainloop()