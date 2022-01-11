from utilities import *
from rule import *

if __name__ == "__main__":
    examples = read_examples("../data/car.data")
    examples, W = get_rand_examples(examples, 500)
    examples, T = get_rand_examples(examples, 500)
    test = examples

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

    valid_pred = 0
    not_valid_pred = 0
    for example in test:
        if example.value == get_class_with_rules_set(example, rules):
            valid_pred += 1
        else:
            not_valid_pred += 1

    print(f"rules set size: {len(rules)}")
    print(f"test set size: {len(test)}")
    print(f"valid_pred: {valid_pred}")
    print(f"not_valid_pred: {not_valid_pred}")

