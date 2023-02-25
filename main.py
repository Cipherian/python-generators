from functools import wraps
import time

"""
Linked List and Node Class
"""

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def __len__(self) -> int:
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def __str__(self) -> str:
        current = self.head
        string = ""
        while current:
            string += f'{current.value} -> '
            current = current.next
        return string

    def __eq__(self, other) -> bool:
        current = self.head
        string = ""
        while current:
            string += f'{current.value} -> '
            current = current.next

        current = other.head
        other_string = ""
        while current:
            other_string += f'{current.value} -> '
            current = current.next

        return string == other_string


    def __iter__(self):
        """
        creates an iterable of the linked list object
        :return: Node
        """
        current = self.head
        while current:
            yield current
            current = current.next

class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


"""
Wrappers
"""

def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper


def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds.")
        return result
    return wrapper


@count_calls
@time_it
def sum_node_values2(ll):
    return sum([current.value for current in ll])






if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    linked_list.append(6)
    linked_list.append(7)
    linked_list.append(8)
    linked_list.append(9)
    linked_list2 = LinkedList()
    linked_list2.append(1)
    linked_list2.append(2)
    linked_list2.append(3)
    linked_list2.append(4)
    linked_list2.append(5)
    linked_list2.append(6)
    linked_list2.append(7)
    linked_list2.append(8)
    linked_list2.append(9)
    print(linked_list)
    print(sum_node_values2(linked_list))
    print(sum_node_values2(linked_list))
    print(sum_node_values2.count) #2
    print(sum_node_values2(linked_list))
    print(sum_node_values2(linked_list))
    print(sum_node_values2.count)  # 4
    if linked_list == linked_list2:
        print("linked lists are equal")



