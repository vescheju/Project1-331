class DLLError(Exception):
    """
    Class representing an error related to the DLL class implemented below.
    """
    pass


class DLLNode:
    """
    Class representing a node in the doubly linked list implemented below.
    """

    def __init__(self, value, next=None, prev=None):
        """
        Constructor
        @attribute value: the value to give this node
        @attribute next: the next node for this node
        @attribute prev: the previous node for this node
        """
        self.next = next
        self.prev = prev
        self.value = value

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)


class DLL:
    """
    Class representing a doubly linked list.
    """

    def __init__(self):
        """
        Constructor
        @attribute head: the head of the linked list
        @attribute tail: the tail of the linked list
        @attribute size: the size of the linked list
        """
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        """
        iterates through the linked list to generate a string representation
        :return: string representation of the linked list
        """
        res = ""
        node = self.head
        while node:
            res += str(node)
            if node.next:
                res += " "
            node = node.next
        return res

    def __str__(self):
        """
        iterates through the linked list to generate a string representation
        :return: string representation of the linked list
        """
        res = ""
        node = self.head
        while node:
            res += str(node)
            if node.next:
                res += " "
            node = node.next
        return res

    ######### MODIFY BELOW ##########

    def is_empty(self):
        """
        Determines if the linked list is empty or not
        :return: [boolean] true if DLL is empty, false otherwise
        """
        return bool(not self.size)

    def insert_front(self, value):
        """
        Inserts a value into the front of the list
        :param value: the value to insert
        """
        if self.is_empty():
            self.head = DLLNode(value)
            self.tail = self.head
            self.size += 1
        else:
            self.head.prev = DLLNode(value, self.head, None)
            self.head = self.head.prev
            self.size += 1

    def insert_back(self, value):
        """
        Inserts a value into the back of the list
        :param value: the value to insert
        """
        if self.is_empty():
            self.head = DLLNode(value)
            self.tail = self.head
            self.size += 1
        else:
            if self.head.next is None:
                self.head.next = DLLNode(value, None, self.head)
                self.tail = self.head.next
                self.size += 1
            else:
                new_tail = DLLNode(value, None, self.tail)
                self.tail.next = new_tail
                self.tail = new_tail
                self.size += 1

    def delete_front(self):
        """
        Deletes the front node of the list
        """
        if self.is_empty():
            raise DLLError()
        if self.size == 1:
            self.head = None
            self.tail = None
            if self.size == 1:
                self.size -= 1
        elif self.size == 2:
            self.head = self.head.next
            self.head.prev = None
            self.tail = self.head
            self.size -= 1
        else:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1

    def delete_back(self):
        """
        Deletes the back node of the list
        """
        if self.is_empty():
            raise DLLError()
        if self.size == 1:
            self.head = None
            self.tail = None
            if self.size == 1:
                self.size -= 1
        elif self.size == 2:
            self.tail = self.tail.prev
            self.tail.next = None
            self.head = self.tail
            self.size -= 1
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1

    def delete_value(self, value):
        """
        Deletes the first instance of the value in the list.
        :param value: The value to remove
        """
        if self.is_empty():
            raise DLLError()
        node = self.head
        size = self.size
        while node is not None:
            if node.value == value:
                if self.size == 1:
                    self.head = None
                    self.tail = None
                    self.size = 0
                    node = None
                elif node.prev is None:
                    self.delete_front()
                elif node.next is None:
                    self.delete_back()
                else:
                    node.next.prev = node.prev
                    node.prev.next = node.next
                    self.size -= 1
                break
            node = node.next
        if size == self.size:
            raise DLLError()

    def delete_all(self, value):
        """
        Deletes all instances of the value in the list
        :param value: the value to remove
        """
        if self.is_empty():
            raise DLLError()
        node = self.head
        size = self.size
        while node is not None:
            if node.value == value:
                if self.size == 1:
                    self.head = None
                    self.tail = None
                    self.size = 0
                    break
                elif node.prev is None:
                    self.delete_front()
                    node = self.head
                elif node.next is None:
                    self.delete_back()
                    break
                else:
                    node.next.prev = node.prev
                    node.prev.next = node.next
                    self.size -= 1
                    node = node.next
            else:
                node = node.next
        if size == self.size:
            raise DLLError()

    def find_first(self, value):
        """
        Finds the first instance of the value in the list
        :param value: the value to find
        :return: [DLLNode] the first node containing the value
        """
        if self.is_empty():
            raise DLLError()
        node = self.head
        while node is not None:
            if node.value == value:
                return node

            node = node.next
        raise DLLError()

    def find_last(self, value):
        """
        Finds the last instance of the value in the list
        :param value: the value to find
        :return: [DLLNode] the last node containing the value
        """
        if self.is_empty():
            raise DLLError()
        node = self.head
        return_node = None
        while node is not None:
            if node.value == value:
                return_node = node
            node = node.next
        if return_node is None:
            raise DLLError()
        return return_node

    def find_all(self, value):
        """
        Finds all of the instances of the value in the list
        :param value: the value to find
        :return: [List] a list of the nodes containing the value
        """
        found_list = []
        if self.is_empty():
            raise DLLError()
        node = self.head
        while node is not None:
            if node.value == value:
                found_list.append(node)
            node = node.next
        if len(found_list) == 0:
            raise DLLError()
        return found_list

    def count(self, value):
        """
        Finds the count of times that the value occurs in the list
        :param value: the value to count
        :return: [int] the count of nodes that contain the given value
        """
        node = self.head
        count = 0
        while node is not None:
            if node.value == value:
                count += 1
            node = node.next
        return count

    def sum(self):
        """
        Finds the sum of all nodes in the list
        :param start: the indicator of the contents of the list
        :return: the sum of all items in the list
        """
        list_sum = None
        node = self.head
        while node is not None:
            if list_sum is None:
                list_sum = node.value
            else:
                list_sum += node.value
            node = node.next
        return list_sum


def reverse(LL):
    """
    Reverses a linked list in place
    :param LL: The linked list to reverse
    """
    if LL.size == 2 or LL.size == 3:
        temp_val = LL.head.value
        LL.head.value = LL.tail.value
        LL.tail.value = temp_val
    if LL.size > 3:
        half_size = int(LL.size / 2)
        node = LL.head
        temp_val = node.value
        half_node = LL.tail
        for i in range(half_size):
            if i == 0:
                LL.head.value = LL.tail.value
                LL.tail.value = temp_val
            else:
                node.value = half_node.value
                half_node.value = temp_val
            node = node.next
            temp_val = node.value
            half_node = half_node.prev
