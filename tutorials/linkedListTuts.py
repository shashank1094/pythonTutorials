class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


head = None
tail = None


def insert_at_end(x):
    global head
    global tail
    if head is None and tail is None:
        head = tail = ListNode(x)
        return
    temp = ListNode(x)
    tail.next = temp
    tail = temp


insert_at_end(1)
insert_at_end(2)
insert_at_end(3)
insert_at_end(4)
insert_at_end(5)


def print_all(start):
    temp = start
    while temp is not None:
        print(temp.val, end=' ')
        temp = temp.next
    print()


print_all(head)


def reverse_it(start):
    if start.next is None:
        return start
    prev = None
    curr = start
    ncur = start.next
    while ncur:
        curr.next = prev
        prev = curr
        curr = ncur
        ncur = ncur.next
    curr.next = prev
    return curr


# noinspection PyTypeChecker
head = reverse_it(head)
print('After reversing')
print_all(head)
