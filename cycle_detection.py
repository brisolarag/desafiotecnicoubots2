def has_cycle(head):
    itr1=itr2=head
    while itr2 and itr2.next:
        itr1=itr1.next
        itr2=itr2.next.next
        if itr1==itr2:
            return 1
    return 0