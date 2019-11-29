import numpy
from time import sleep

def sleepy(time2sleep):
    sleep(time2sleep)
    
def supersleepy(time2sleep):
    sleep(time2sleep)
    
def randmatmul(n=1000):
    a = numpy.random.random((n,n))
    b = a @ a
    return b
    
def useless(a):
    if not isinstance(a, int):
        return
    
    randmatmul(a)
    
    ans = 0
    for i in range(a):
        ans += i
        
    sleepy(1.0)
    supersleepy(2.0)
    
    print("Done")
    return ans

#@profile
def runner():
    useless(1000)

    
runner()