from utilities import *
from rule import *

if __name__ == "__main__":
    examples = read_examples("../data/car.data")
    examples, W = get_rand_examples(examples, 500)
    examples, T = get_rand_examples(examples, 500)

    rules = []
    R = deepcopy(T)

    while len(R) != 0:
        k = aq_specialization(R, W)
        d = get_prevail_class(k, R)
        rules.append(Rule(k, d))
        R = remove_from_set(k, R)
        W = remove_from_set(k, W)

#    for i, r in enumerate(rules):
#        print(f"rule {i}: {r}")


