from rpc import RPCClient
client=RPCClient('127.0.0.1', 8080)
client.connect()

print(client.add(5, 6))
print(client.sub(5, 6))

# client.disconnect()

# 172.23.96.1, 192.168.56.1, 192.168.0.167