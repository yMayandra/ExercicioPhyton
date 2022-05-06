import Control

def exercicio1(a, b):
    c = a
    a = b
    b = c
    return 'A={} B={}'.format(a, b)