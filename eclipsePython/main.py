'''
Created on 2012-7-4

@author: jacob
'''

if __name__ == '__main__':
    pass

def printMax(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.hahah'''
    x = int(x) # convert to integers, if possible
    y = int(y)

    if x > y:
        print x, 'is maximum'
    else:
        print y, 'is maximum'

printMax(3, 5)
print printMax.__doc__

