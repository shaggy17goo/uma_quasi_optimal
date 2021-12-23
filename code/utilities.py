from collections import Counter
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
    ret = []
    shuffle(examples)
    while len(ret) < count:
        ret.append(examples.pop())
    return examples, ret


def get_prevail_class(com, set):
    classes = []
    for example in set:
        if is_more_general(com, example.complex):
            classes.append(example.value)
    dict_count = Counter(classes)
    x = max(dict_count, key=dict_count.get)
    print(f"{com}\n"
          f"DICT: {dict_count}\n\n")
    return x


def remove_from_set(com, set):
    new_set = []
    for example in set:
        if not is_more_general(com, example.complex):
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


def examples_covered_by_complexes(complexes, set):
    covered = []
    for example in set:
        for c in complexes:
            if is_more_general(c, example.complex):
                covered.append(example)
                break
    return covered


def remove_more_general_complexes(complexes):
    # remove more general
    i = 0
    while i < len(complexes):
        j = 0
        while j < len(complexes):
            if not complexes[i].__eq__(complexes[j]) and is_more_general(complexes[i], complexes[j]):
                complexes.pop(i)
                i -= 1
                break
            j += 1
        i += 1

    # remove duplicate
    i = 0
    while i < len(complexes):
        j = i + 1
        while j < len(complexes):
            if complexes[i].__eq__(complexes[j]):
                complexes.pop(j)
                j -= 1
            j += 1
        i += 1

    return complexes


def do_complexes_specialization(G, pos_seed, neg_seed):
    new_G = []
    for c in G:
        spec_complexes = specialization(c, pos_seed.complex, neg_seed.complex)
        for spec_c in spec_complexes:
            new_G.append(spec_c)
        else:
            new_G.append(c)
    return new_G


def give_best_x_complexes(pos_seed, G, W, cnt):
    W_1, W_0 = divide_set_by_class(pos_seed.value, W)
    scores = {}
    bests = []
    for idx, com in enumerate(G):
        tp = 0
        tn = 0
        fp = 0
        fn = 0
        for ex in W_0:
            if len(examples_covered_by_complexes([com], [ex])) == 1:
                fp += 1
            elif len(examples_covered_by_complexes([com], [ex])) == 0:
                tn += 1
        for ex in W_1:
            if len(examples_covered_by_complexes([com], [ex])) == 1:
                tp += 1
            elif len(examples_covered_by_complexes([com], [ex])) == 0:
                fn += 1
        scores[str(idx)] = tp + tn - fp - fn

    i = 0
    while i < cnt and len(scores) > 0:
        best = max(scores, key=scores.get)
        bests.append(G[int(best)])
        del scores[best]
        i += 1
    return bests


def aq_specialization(R, W):
    G = [get_full_complex()]
    pos_seed = R[randint(0, len(R) - 1)]
    R_1, R_0 = divide_set_by_class(pos_seed.value, R)
    while len(examples_covered_by_complexes(G, R_0)) != 0:
        neg_seed = R_0.pop(randint(0, len(R_0) - 1))
        G = do_complexes_specialization(G, pos_seed, neg_seed)
        G = remove_more_general_complexes(G)
        G = give_best_x_complexes(pos_seed, G, W, 10)
    return give_best_x_complexes(pos_seed, G, W, 1)[0]
