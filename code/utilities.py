from copy import *
from random import *

from example import *


def get_more_general(first, second):
    if (is_more_general(first, second)):
        return first
    elif (is_more_specific(first, second)):
        return second
    else:
        return None


def is_more_general(first, second):
    if not all(elem in first.buying for elem in second.buying):
        return 0
    if not all(elem in first.maint for elem in second.maint):
        return 0
    if not all(elem in first.doors for elem in second.doors):
        return 0
    if not all(elem in first.persons for elem in second.persons):
        return 0
    if not all(elem in first.lug_boot for elem in second.lug_boot):
        return 0
    if not all(elem in first.safety for elem in second.safety):
        return 0
    return 1


def is_more_specific(first, second):
    if not all(elem in second.buying for elem in first.buying):
        return 0
    if not all(elem in second.maint for elem in first.maint):
        return 0
    if not all(elem in second.doors for elem in first.doors):
        return 0
    if not all(elem in second.persons for elem in first.persons):
        return 0
    if not all(elem in second.lug_boot for elem in first.lug_boot):
        return 0
    if not all(elem in second.safety for elem in first.safety):
        return 0
    return 1


def specialization(k, pos_seed, neg_seed):
    ret = []
    for a in k.buying:
        temp = deepcopy(k)
        temp.buying.remove(a)
        if is_more_general(temp, pos_seed) == 1 and is_more_general(temp, neg_seed) == 0:
            ret.append(temp)
    for a in k.maint:
        temp = deepcopy(k)
        temp.maint.remove(a)
        if is_more_general(temp, pos_seed) == 1 and is_more_general(temp, neg_seed) == 0:
            ret.append(temp)
    for a in k.doors:
        temp = deepcopy(k)
        temp.doors.remove(a)
        if is_more_general(temp, pos_seed) == 1 and is_more_general(temp, neg_seed) == 0:
            ret.append(temp)
    for a in k.persons:
        temp = deepcopy(k)
        temp.persons.remove(a)
        if is_more_general(temp, pos_seed) == 1 and is_more_general(temp, neg_seed) == 0:
            ret.append(temp)
    for a in k.lug_boot:
        temp = deepcopy(k)
        temp.lug_boot.remove(a)
        if is_more_general(temp, pos_seed) == 1 and is_more_general(temp, neg_seed) == 0:
            ret.append(temp)
    for a in k.safety:
        temp = deepcopy(k)
        temp.safety.remove(a)
        if is_more_general(temp, pos_seed) == 1 and is_more_general(temp, neg_seed) == 0:
            ret.append(temp)
    return ret


def read_examples(path):
    examples = []
    file = open(path, "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        split_line = line.split(',')
        examples.append(
            Example(split_line[0], split_line[1], split_line[2], split_line[3], split_line[4], split_line[5],
                    split_line[6][:-1]))
    return examples


def get_rand_examples(examples, count):
    ret =[]
    shuffle(examples)
    while len(ret) < count:
        ret.append(examples.pop())
    return examples, ret

