#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    Given a package with a weight limit `limit` and a list `weights` of item
    weights, implement a function `get_indices_of_item_weights` that finds two
    items whose sum of weights equals the weight limit `limit`. Your function
    will return an instance of an `Answer` tuple that has the following form:
        (zero, one)
    where each element represents the item weights of the two packages.
    The higher valued index should be placed in the `zeroth` index and the
    smaller index should be placed in the `first` index. If such a pair
    doesn’t exist for the given inputs, your function should return `None`.

    Your solution should run in linear time.
    Example:
        input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
        output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
    """
    # PLAN
    # loop over weight, put into hash table, key is weight value is index
    # need to handle duplicate values somehow
    for i in range(0, length):
        weight = weights[i]
        # If not duplicate simply insert weight as key, index list with one item as value
        if hash_table_retrieve(ht, weight) is None:
            # print(f"weight: {weight} ; i: {i}")
            hash_table_insert(ht, weight, list([i]))
        # If duplicate append new index to list stored as value and overwrite key/value pair
        else: 
            indexList = hash_table_retrieve(ht, weight)
            # print(f"before indexList:{indexList}")
            indexList.append(i)
            # print(f"after indexList:{indexList}")
            hash_table_insert(ht, weight, indexList)

    # loop over hash table (16 indices)
    for weight in weights:
        # check to see if a complementary weight in table
        if hash_table_retrieve(ht, limit - weight) is not None:
            # print(f"Limit: {limit} ; Weight: {weight} ; limit - weight : {limit-weight}")
            # if complimentary weights are the same, get both indices from list. Second one will always be bigger.
            if hash_table_retrieve(ht, weight)[0] == hash_table_retrieve(ht, limit - weight)[0]:
                bigIndex = hash_table_retrieve(ht, weight)[1]
                littleIndex = hash_table_retrieve(ht, weight)[0]
            # if complimentary weight exists, see which index value stored in the 0th position is bigger
            elif hash_table_retrieve(ht, weight)[0] > hash_table_retrieve(ht, limit - weight)[0]:
                bigIndex = hash_table_retrieve(ht, weight)[0]
                littleIndex = hash_table_retrieve(ht, limit - weight)[0]
            else:
                bigIndex = hash_table_retrieve(ht, limit - weight)[0]
                littleIndex = hash_table_retrieve(ht, weight)[0]
            # return tuple
            # print (f"bigIndex: {bigIndex} ; littleIndex: {littleIndex} ")
            return (bigIndex, littleIndex)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
