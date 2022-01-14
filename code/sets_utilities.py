from aq_utilities import *
from complex import *
from random import shuffle


def get_rand_examples(examples, count):
    ret = []
    shuffle(examples)
    while len(ret) < count:
        ret.append(examples.pop())
    return examples, ret


def remove_from_set(com, set):
    new_set = []
    for example in set:
        if not is_more_general_complex(com, example.complex):
            new_set.append(example)
    return new_set


def divide_set_by_class(c, set):
    is_class = []
    is_not_class = []
    for example in set:
        if example.value == c:
            is_class.append(example)
        else:
            is_not_class.append(example)
    return is_class, is_not_class
