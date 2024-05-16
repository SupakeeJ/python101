name = "Dave"
count = 2
color = "pink"

def another():
    color = "blue"
    global count
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Dave")

def color1():
    print(color)
another()
color1()