import random
import string

class Node:
    def __init__(self, key, keyring):
        self.key = key
        self.keyring = keyring
        self.next = None

class DynamicLinearList:
    def __init__(self):
        self.head = None

    def find(self, key):
        current = self.head
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None
        
    def show(self):
        current = self.head
        while current:
            print(f"Key: {current.key}, Keyring: {current.keyring}")
            current = current.next

    def insert(self, key, keyring):
        if self.find(key):
            print("Element with the specified key already exists.")
            return
        new_node = Node(key, keyring)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, key):
        current = self.head
        if current and current.key == key:
            self.head = current.next
            return
        prev = None
        while current:
            if current.key == key:
                prev.next = current.next
                return
            prev = current
            current = current.next
        print("Element not found.")

list1 = DynamicLinearList()
list2 = DynamicLinearList()

print("List 1:")
list1.show()
print("List 2:")
list2.show()

list1.insert("Kyrylo, Mark", random.randint(0, 100))

for _ in range(2):
    random_key = ''.join(random.choices(string.ascii_lowercase, k=5))
    list1.insert(random_key, random.randint(0, 100))

list1.insert("Algorithms", random.randint(0, 100))

for _ in range(2):
    random_key = ''.join(random.choices(string.ascii_lowercase, k=5))
    list1.insert(random_key, random.randint(0, 100))

list1.insert("Skyrtach, Volobuiev", random.randint(0, 100))

list2.insert("Dominik", random.randint(0, 100))

for _ in range(2):
    random_key = ''.join(random.choices(string.ascii_lowercase, k=5))
    list2.insert(random_key, random.randint(0, 100))

list2.insert("Data structures", random.randint(0, 100))

for _ in range(2):
    random_key = ''.join(random.choices(string.ascii_lowercase, k=5))
    list2.insert(random_key, random.randint(0, 100))

list2.insert("Rynkiewicz", random.randint(0, 100))

print(" ")
list1.show()
print(" ")
list2.show()

print ("      ")

element5 = list1.find("Algorithms")
element10 = list2.find("Data structures")
if element5:
    print(f"Key: {element5.key}, Keyring: {element5.keyring}")
else:
    print("Element with key 'Algorithms' not found.")
if element10:
    print(f"Key: {element10.key}, Keyring: {element10.keyring}")
else:
    print("Element with key 'Data structures' not found.")
print("     ")

list1.delete("Algorithms")
list2.delete("Data structures")

print(" ")
list1.show()
print(" ")
list2.show()
