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
    # need to handle double values somehow
    for i in range(0, length - 1):
        hash_table_insert(ht, weights[i], i)
    # loop over hash table (16 indices)
    for weight in weights:
        # check to see if a complementary weight in table
        if hash_table_retrieve(ht, limit - weight) is not None:
            print(f"Limit: {limit} ; Weight: {weight} ; limit - weight : {limit-weight}")
            # if complimentary weight exists, see which one is bigger
            if hash_table_retrieve(ht, weight) >= hash_table_retrieve(ht, limit - weight):
                bigIndex = hash_table_retrieve(ht, weight)
                littleIndex = hash_table_retrieve(ht, limit - weight)
            else:
                bigIndex = hash_table_retrieve(ht, limit - weight)
                littleIndex = hash_table_retrieve(ht, weight)
            # return tuple
            print (f"bigIndex: {bigIndex} ; littleIndex: {littleIndex} ")
            return (bigIndex, littleIndex)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
