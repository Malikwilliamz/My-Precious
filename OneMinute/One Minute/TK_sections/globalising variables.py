def naming():
    global name
    name = 'malik'

def hello_name():
    global name
    print(name + 'hello')

naming()
hello_name()
print(name)
