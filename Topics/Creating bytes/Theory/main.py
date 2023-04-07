#  You can experiment here, it won’t be checked

message = input("message string: ")
key = int(input("key: "))


myBytes = key.to_bytes(2, "little")

sum = 0
for bit in myBytes:
    sum += bit

orders = []
for i in message:
    orders.append(ord(i) + sum)

print("".join([chr(order) for order in orders]))



