from aq_utilities import *


def test_rules(rules, test):
    valid_pred = 0
    not_valid_pred = 0
    for example in test:
        if example.value == get_class_with_rules_set(example, rules):
            valid_pred += 1
        else:
            not_valid_pred += 1

    print(f"accuracy: {valid_pred / len(test)}")
    print(f"rules set size: {len(rules)}")
    print(f"test set size: {len(test)}")
    print(f"valid_pred: {valid_pred}")
    print(f"not_valid_pred: {not_valid_pred}")

def get_class_with_rules_set(example, rules):
    for rule in rules:
        if is_more_general_complex(rule.complex, example.complex):
            return rule.value

def print_rules(rules):
    for i, r in enumerate(rules):
        print(f"rule {i}: {r}")
