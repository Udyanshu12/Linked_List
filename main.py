from linked_list import LinkedList
from node import Node

node1 = Node(5)
my_list = LinkedList(node1)

node2 = Node(6)
my_list.append(node2)
my_list.append(Node(7))
my_list.append(Node(8))

my_list.pop()
my_list.prepend(Node(4))
my_list.prepend(Node(3))

my_list.set(0, 0)
my_list.insert(1, Node(1))
my_list.insert(2, Node(2))
my_list.insert(3, Node(3))

my_list.remove(0)
my_list.reverse()
my_list.print_list()
