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
    route = [None] * (length - 1)

    """
    YOUR CODE HERE
    """
    # put all tickets into the hashtable with source as key and destination as value
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    # initialize source for loop
    source = "NONE"
    for i in range(0, length - 1):
        destination = hash_table_retrieve(hashtable, source)
        # if destination is not "NONE":
        route[i] = destination
        source = destination

    return route
