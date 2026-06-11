def message1():
    message2()
    print('hello')

def message2():
    message3()
    print('hello')

def message3():
    message4()
    print('hello')

def message4():
    message5()
    print('hello')

def message5():
    print('hello')

message1()

'''
debug this file to see the stack calls in pycharm.
after message 5 reutrn not needed because program finished without any conditions.

'''