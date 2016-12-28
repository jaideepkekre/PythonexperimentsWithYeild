def fibonacci():
    yield 1
    yield 1
    a , b = 1,1  
    while True :
        yield a+b 
        c=b
        b=a+b 
        a=c        
        
fibogen = fibonacci() 
print (next(fibogen)) 
print (next(fibogen)) 
print (next(fibogen)) 
print (next(fibogen)) 
print (next(fibogen)) 
print (next(fibogen)) 