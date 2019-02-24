import stack1


stack1.push('spam')
stack1.push(123)
#display the top of the stack
stack1.top()

stack1.stack
stack1.pop()

stack1.dump()
stack1.pop()


stack1.empty()

for c in 'spam': stack1.push(c)

while not stack1.empty():
	print(stack1.pop(),end=' ')

stack1.pop()