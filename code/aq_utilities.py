from datetime import datetime
from main import *
from sets_utilities import *
from example import *
from rule import *
from collections import Counter
from copy import deepcopy
from random import randint


def generate_rules(R, W):
    rules = []
    while len(R) != 0:
        k = aq_specialization(R, W)
        d = get_dominate_class(k, R)
        rules.append(Rule(k, d))
        R = remove_from_set(k, R)
        W = remove_from_set(k, W)

    return rules


def aq_specialization(R, W):
    while True:
        G = [get_full_complex()]
        pos_seed = R[randint(0, len(R) - 1)]
        R_1, R_0 = divide_set_by_class(pos_seed.value, R)
        while len(examples_covered_by_complexes(G, R_0)) != 0:
            if custom_neg_seed:
                neg_seed = R_0.pop(get_better_neg_seed(R_0, pos_seed))
            else:
                neg_seed = R_0.pop(randint(0, len(R_0) - 1))
            G = do_complexes_specialization(G, pos_seed, neg_seed)
            G = remove_more_specific_complexes(G)
            G = give_best_x_complexes(pos_seed, G, W, best_complexes_param)

        best = give_best_x_complexes(pos_seed, G, W, 1)[0]

        # Own additional function, minimizes rule set size, increases computational cost
        matches = len(examples_covered_by_complexes([best], R))
        if matches > minimize_rules_cnt_param * len(R):
            return best
        # Own additional function, minimizes rule set size, increases computational cost


def do_complexes_specialization(G, pos_seed, neg_seed):
    new_G = []

    for c in G:
        if is_more_general_complex(c, neg_seed.complex) == 0:
            new_G.append(c)
        else:
            spec_complexes = complex_specialization(c, pos_seed.complex, neg_seed.complex)
            for spec_c in spec_complexes:
                new_G.append(spec_c)
    return new_G


def complex_specialization(k, pos_seed, neg_seed):
    ret = []
    for a in k.buying:
        temp = deepcopy(k)
        temp.buying.remove(a)
        if is_more_general_complex(temp, pos_seed) == 1 and is_more_general_complex(temp, neg_seed) == 0:
            ret.append(temp)
    for a in k.maint:
        temp = deepcopy(k)
        temp.maint.remove(a)
        if is_more_general_complex(temp, pos_seed) == 1 and is_more_general_complex(temp, neg_seed) == 0:
            ret.append(temp)
    for a in k.doors:
        temp = deepcopy(k)
        temp.doors.remove(a)
        if is_more_general_complex(temp, pos_seed) == 1 and is_more_general_complex(temp, neg_seed) == 0:
            ret.append(temp)
    for a in k.persons:
        temp = deepcopy(k)
        temp.persons.remove(a)
        if is_more_general_complex(temp, pos_seed) == 1 and is_more_general_complex(temp, neg_seed) == 0:
            ret.append(temp)
    for a in k.lug_boot:
        temp = deepcopy(k)
        temp.lug_boot.remove(a)
        if is_more_general_complex(temp, pos_seed) == 1 and is_more_general_complex(temp, neg_seed) == 0:
            ret.append(temp)
    for a in k.safety:
        temp = deepcopy(k)
        temp.safety.remove(a)
        if is_more_general_complex(temp, pos_seed) == 1 and is_more_general_complex(temp, neg_seed) == 0:
            ret.append(temp)
    return ret


def get_dominate_class(com, set):
    classes = []
    for example in set:
        if is_more_general_complex(com, example.complex):
            classes.append(example.value)
    dict_count = Counter(classes)
    dominate_class = max(dict_count, key=dict_count.get)

    # DEBUG BLOCK
    if debug_on:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"{com}\n DICT: {dict_count}, R size: {len(set)}\nCurrent Time = {current_time}\n")
    # DEBUG BLOCK

    return dominate_class


def examples_covered_by_complexes(complexes, set):
    covered = []
    for example in set:
        for c in complexes:
            if is_more_general_complex(c, example.complex):
                covered.append(example)
                break
    return covered


def remove_more_specific_complexes(complexes):
    # remove more specific
    i = 0
    while i < len(complexes):
        j = 0
        while j < len(complexes):
            if not complexes[i].__eq__(complexes[j]) and is_more_specific_complex(complexes[i], complexes[j]):
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


def get_better_neg_seed(R_0, pos_seed):
    neg_seed_index = 0
    neg_seed_distance = get_distance_between_examples(R_0[neg_seed_index], pos_seed)
    for idx, example in enumerate(R_0):
        if get_distance_between_examples(example, pos_seed) > neg_seed_distance:
            neg_seed_index = idx
            neg_seed_distance = get_distance_between_examples(example, pos_seed)
    return neg_seed_index
