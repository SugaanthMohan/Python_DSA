"""
Singly linked list
==================

DEFINITION:
============
Singly linked lists contain nodes which have
    a data field    as well as
    'next' field,
    which points to the next node in line of nodes.
    Operations that can be performed on singly linked lists include
    insertion,
    deletion and
    traversal.

A singly linked list whose nodes contain two fields:
    an integer value     and
    a link to the next node


The following code demonstrates how to add a new node with data "value"
to the end of a singly linked list:

node addNode(node head, int value) {
    node temp, p; // declare two nodes temp and p
    temp = createNode(); // assume createNode creates a new node with data = 0 and next pointing to NULL.
    temp->data = value; // add element's value to data part of node
    if (head == NULL) {
        head = temp;     // when linked list is empty
    }
    else {
        p = head; // assign head to p
        while (p->next != NULL) {
            p = p->next; // traverse the list until p is the last node. The last node always points to NULL.
        }
        p->next = temp; // Point the previous last node to the new node created.
    }
    return head;
}
"""
from Data_Structures.LinkedList.Node import Node
from copy import copy as duplicate


class LinkedList(object):

    __slots__ = (
        'head',
        'size'
    )

    def __init__(self, head=None):
        self.head = head
        if self.head:
            self.size = 1
        else:
            self.size = 0
        self.print_all()

    def add_node(self, data):
        self.size += 1
        if self.head is None:
            self.head = Node(data)
            self.print_all()
        else:
            my_node = Node(data)
            my_node.update_next(duplicate(self.head))
            self.head = my_node
            self.print_all()

    def delete_node(self, data):

        if self.head is None:
            raise Exception("Empty Singly Linked List")
        else:
            # SET CURRENT NODE INFO
            if self.head.data == data:
                self.head = self.head.next_node
                self.size -= 1
                self.print_all()
                return
            else:
                # SEQUENTIAL SEARCH
                curr_obj = self.head
                while True:
                    if curr_obj.next_node.data == data:
                        if curr_obj.next_node.next_node is None:
                            curr_obj.next_node = None
                            self.size -= 1
                            self.print_all()
                            return
                        else:
                            curr_obj.next_node = curr_obj.next_node.next_node
                            self.size -= 1
                            self.print_all()
                            return
                    else:
                        pass
                    curr_obj = curr_obj.next_node
                raise Exception("Element Not Found in List")

    def print_all(self):

        print("========================")
        if self.head is None:
            print("Empty Linked List")
        else:
            curr_obj = self.head
            while curr_obj is not None:
                print(curr_obj.data)
                curr_obj = curr_obj.next_node

    def __len__(self):
        return self.size


if __name__ == '__main__':
    obj = LinkedList()
    obj.add_node(10)
    obj.add_node(20)
    obj.add_node(30)
    obj.delete_node(20)
    obj.delete_node(10)
    obj.delete_node(30)

