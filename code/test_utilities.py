from aq_utilities import *


def test_rules(rules, test):
    valid_pred = 0
    not_valid_pred = 0
    for example in test:
        if example.value == get_class_with_rules_set(example, rules):
            valid_pred += 1
        else:
            not_valid_pred += 1
    return valid_pred / len(test)


def test_rules_sets_with_voting(rules_sets, test):
    scores = [{} for _ in range(len(test))]
    for idx, example in enumerate(test):
        for rules in rules_sets:
            try:
                scores[idx][get_class_with_rules_set(example, rules)] += 1
            except:
                scores[idx][get_class_with_rules_set(example, rules)] = 1

    final_score = 0
    for idx, example in enumerate(test):
        if example.value == max(scores[idx], key=scores[idx].get):
            final_score += 1

    return final_score / len(test)


def get_class_with_rules_set(example, rules):
    for rule in rules:
        if is_more_general_complex(rule.complex, example.complex):
            return rule.value

def print_rules(rules):
    for i, r in enumerate(rules):
        print(f"rule {i}: {r}")
