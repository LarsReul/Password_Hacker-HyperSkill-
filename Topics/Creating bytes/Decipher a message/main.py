message = input()
key = int(input())


myBytes = key.to_bytes(2, "little")

sum = 0
for bit in myBytes:
    sum += bit

orders = []
for i in message:
    orders.append(ord(i) + sum)

print("".join([chr(order) for order in orders]))



