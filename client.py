from rpc import RPCClient
server=RPCClient('127.0.0.1', 8080)
server.connect()

print(server.add(5, 6))
print(server.sub(5, 6))
print(server.factorial(5))

# client.disconnect()

# 172.23.96.1, 192.168.56.1, 192.168.0.167