fib = lambda x: x if (x==1 or x==0) else fib(x-1)+fib(x-2)
if __name__=="__main__":
    print([fib(x) for x in range(10)])
    