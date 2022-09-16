#---------------------Fibonaci sequence--------------------------------#


def fib(num):
   a = 0
   b = 1
   for i in range(num):
    yield a 
    temp = a 
    a = b
    b = temp + b
