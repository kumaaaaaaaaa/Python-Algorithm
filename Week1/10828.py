import sys

def push(x):
    stack.append(x)
def pop():  
    if(not stack):
        return -1
    else:
        return stack.pop()

def size():
    return len(stack)

def empty():
    if(stack):
        return 0
    else:
        return 1

def top():
    if(stack):
        return stack[-1]
    else:
        return -1


n = int(sys.stdin.readline())
stack = []
for i in range(n):
    input_split = sys.stdin.readline().rstrip().split()

    order = input_split[0]

    if order == "push":
        push(input_split[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "top":
        print(top())