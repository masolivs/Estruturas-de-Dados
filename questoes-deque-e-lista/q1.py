class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_front(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_back(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_front(self):
        if not self.head:
            return None
        value = self.head.value
        self.head = self.head.next
        return value

    def remove_back(self):
        if not self.head:
            return None
        value = self.tail.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current
        return value

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

def main():
    linked_list = LinkedList()
    while True:
        command = input()
        if command[0] == 'X':
            break
        elif command[0] == 'I':
            _, value = command.split()
            linked_list.insert_front(int(value))
        elif command[0] == 'F':
            _, value = command.split()
            linked_list.insert_back(int(value))
        elif command[0] == 'P':
            removed_value = linked_list.remove_back()
            if removed_value is not None:
                print(removed_value)
        elif command[0] == 'D':
            removed_value = linked_list.remove_front()
            if removed_value is not None:
                print(removed_value)

    linked_list.print_list()


if __name__ == "__main__":
    main()
