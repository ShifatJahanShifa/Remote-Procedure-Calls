# Remote-Procedure-Calls

## Components and Interactions
### RPCServer:

```
__init__: Initializes the server.
registerInstance: Registers methods of an instance.
run: Starts the server and listens for connections.
__handle__: Handles client requests in a separate thread.
```
### RPCClient:

```
__init__: Initializes the client.
connect: Connects to the server.
disconnect: Disconnects from the server.
__getattr__: Dynamically handles method calls.
``` 

## Sequence of Operations
### Server:

```
Initialize (RPCServer.__init__)
Register instance methods (RPCServer.registerInstance)
Run (RPCServer.run)
```

### Client:

```
Initialize (RPCClient.__init__)
Connect (RPCClient.connect)
Call method (RPCClient.__getattr__ -> execute)
Disconnect (RPCClient.disconnect)
```

### Server Handling:

```
Accept connection (RPCServer.run -> sock.accept)
Handle request (RPCServer.__handle__)
```