from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.__len__() == self.capacity:
            # if current is the tail and buffer full add to head
            if self.current == self.storage.tail:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.storage.head
            # if current is not tail, iterate through buffer list while appending
            else:
                if self.current.next:
                    self.current.next.delete()
                    self.current.insert_after(item)
                    self.current = self.current.next
                else:
                    self.current = self.storage.tail
        # while filling buffer insert backwards from tail
        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        length = 0
        current = self.storage.head
        while length != self.storage.__len__() + 1:
            length += 1
            if current:
                list_buffer_contents.append(current.value)
                current = current.next
            
           
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
