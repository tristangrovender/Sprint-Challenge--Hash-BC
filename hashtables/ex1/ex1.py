#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)
    
    for i in range(len(weights)):
        # number we will be looking for in hashtable to complete a valid pair
        valid_pair = limit - weights[i]


        # searcch hash table for the value that would work
        does_exist = hash_table_retrieve(ht, valid_pair)

        if does_exist:
            print(does_exist, i)
            return (does_exist, i)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

get_indices_of_item_weights([2, 8, 12, 15, 16], 7, 27)