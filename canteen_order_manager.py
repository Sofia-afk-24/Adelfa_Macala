from itertools import count
from operator import index
from os import remove

orders = []

for i in range(1, 6):
    order = input(f"Enter Order {i}: ")
    orders.append(order)





print(f"Original Orders: [{orders}]")

add_order = input("Enter additional order: ")
print(f"Updated Orders: [{orders}]")
orders.append(add_order)

print(f"Updated Orders: [{orders}]")
pri_order = input("Enter priority order: ")
search = input("Search for an order: ")
cancel_order = input("Enter order to cancel: ")

if search in orders:
    print(f"Number of Occurrences: {count(search)}")
    print(f"First Index: {index(search)}")
else:
    print("Order not found")

print(f"Enter order to cancel: {remove(cancel_order)}")
print(f"Updated Orders: [{orders}]")
