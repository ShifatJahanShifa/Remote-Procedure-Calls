class Calculator:
    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b
    
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)
    
calculator=Calculator()

from rpc import RPCServer

server=RPCServer()

# server.registerMethod(add)
# server.registerMethod(sub)

server = RPCServer()
server.registerInstance(calculator) 

server.run()