#stack implementation using a list
stack = []

#push operation - we will use the append method
stack.append(5)
stack.append(6)
stack.append(9)
stack.append(6)
stack.append(3)

print('Current Stack')
print(stack)
#get the size of the stack
print(f'The stack has {len(stack)} elements')

print(f'The peek element is {stack[-1]}')

#perform 2 pop operations
stack.pop()
stack.pop()
print(f'The peek element after 2 dequeue operations is {stack[-1]}')


