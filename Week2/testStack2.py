from stack2 import Stack

x = Stack()
x.push('spam')
x.push(123)

#display x
x

y = Stack()
y.push(3.1415)
y.push(x.pop())

#display x and y
x,y

z = Stack()

for c in 'spam': z.push(c)

while z:
	print(z.pop(),end=' ')
z = x + y

for item in z:
	print(item,end=' ')
z.reverse()