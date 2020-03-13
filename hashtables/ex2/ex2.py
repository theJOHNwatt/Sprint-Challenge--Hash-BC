#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * int(length-1)

    for x in tickets:
        hash_table_insert(hashtable, x.source, x.destination)
    current_trip = hash_table_retrieve(hashtable, 'NONE')
    for i in range(0, length-1):
        route[i] = current_trip
        next_trip = hash_table_retrieve(hashtable, current_trip)
        current_trip = next_trip
    print(f'Route: {route}')

    return route
