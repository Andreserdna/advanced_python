class Node:
	def __init__(self,element):
		self.element = element
		self.next = None
head = None
tail = None

head = Node('Chicago')
last = head

head = Node("Chicago")
tail = head
tail.next = Node("Denver")
tail = tail.next
tail.next = Node("dallas")
tail = tail.next
current = head
while current != None:
	print(current.element)
	current = current.next

