class Calculator:
    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b
calculator=Calculator()

from rpc import RPCServer

server=RPCServer()

# server.registerMethod(add)
# server.registerMethod(sub)

server = RPCServer()
server.registerInstance(calculator) 

server.run()