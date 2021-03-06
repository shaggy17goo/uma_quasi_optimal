from aq_utilities import *
import shutil
from main import *


def test_rules(rules, test):
    valid_pred = 0
    not_valid_pred = 0
    for example in test:
        if example.value == get_class_with_rules_set(example, rules):
            valid_pred += 1
        else:
            not_valid_pred += 1
    return valid_pred / len(test)


def test_rules_sets_with_voting(path_rules_sets, path_test):
    dir_list = os.listdir(path_rules_sets)
    test = read_examples(path_test)
    rules_sets = []
    ale_rule_cnt = 0
    for i in range(len(dir_list)):
        rules_sets.append(read_rules(f"{path_rules_sets}/rules.{i + 1}.pkl"))
        ale_rule_cnt += len(rules_sets[i])

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

    print(f"Accuracy with voting by {len(dir_list)} rules sets: {final_score/len(test)}")
    print(f"rules cnt: {ale_rule_cnt/len(rules_sets)}")
    return final_score / len(test)


def get_class_with_rules_set(example, rules):
    for rule in rules:
        if is_more_general_complex(rule.complex, example.complex):
            return rule.value


def print_rules(rules):
    for i, r in enumerate(rules):
        print(f"rule {i}: {r}")


def test_generate_and_test_x_rules_sets_voting(x, test_name):
    if not os.path.exists(f"../data/{test_name}/"):
        os.makedirs(f"../data/{test_name}/")
        divide_file_randomly_on_two_parts("../data/car.data", 2 * train_and_wal_size)
        shutil.copyfile("../data/car.dataextracted", f"../data/{test_name}/car.data.tren_wal")
        shutil.copyfile("../data/car.datarest", f"../data/{test_name}/car.data.test")
    for i in range(x):
        examples = read_examples(f"../data/{test_name}/car.data.tren_wal")
        examples, T = get_rand_examples(examples, train_and_wal_size)
        examples, W = get_rand_examples(examples, train_and_wal_size)
        rules = generate_rules(T, W)
        save_rules(rules, f"../data/{test_name}/rules/")

    path_test = f"../data/{test_name}/car.data.test"
    path_rules = f"../data/{test_name}/rules/"
    test_rules_sets_with_voting(path_rules, path_test)


def test_one_rule_generate():
    global debug_on, custom_neg_seed, minimize_rules_cnt_param, train_and_wal_size, best_complexes_param

    divide_file_randomly_on_two_parts("../data/car.data", train_and_wal_size * 2)
    examples = read_examples("../data/car.dataextracted")
    examples, T = get_rand_examples(examples, train_and_wal_size)
    examples, W = get_rand_examples(examples, train_and_wal_size)
    test = read_examples("../data/car.datarest")

    rules = generate_rules(T, W)
    score = test_rules(rules, test)
    print(f"Summary:")
    print(f"rules_cnt: {len(rules)}")
    print(f"accuracy: {score}\n")


def test_diff_best_complexes_param():
    global best_complexes_param

    gen_times = 10
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
        best_complexes_param = i
        acc = 0
        rcnt = 0
        for j in range(gen_times):
            divide_file_randomly_on_two_parts("../data/car.data", train_and_wal_size * 2)
            examples = read_examples("../data/car.dataextracted")
            examples, T = get_rand_examples(examples, train_and_wal_size)
            examples, W = get_rand_examples(examples, train_and_wal_size)
            test = read_examples("../data/car.datarest")

            rules = generate_rules(T, W)
            acc += test_rules(rules, test)
            rcnt += len(rules)

        print(f"Summary for {best_complexes_param}:\n")
        print(f"rules_cnt: {rcnt / gen_times}\n")
        print(f"accuracy: {acc / gen_times}\n\n")


def test_diff_sets_size():
    global train_and_wal_size

    gen_times = 10
    for i in [200, 300, 400, 500, 600, 700, 800]:
        train_and_wal_size = i
        acc = 0
        rcnt = 0
        for j in range(gen_times):
            divide_file_randomly_on_two_parts("../data/car.data", 2 * train_and_wal_size)
            examples = read_examples("../data/car.dataextracted")
            examples, T = get_rand_examples(examples, train_and_wal_size)
            examples, W = get_rand_examples(examples, train_and_wal_size)
            test = read_examples("../data/car.datarest")

            rules = generate_rules(T, W)
            acc += test_rules(rules, test)
            rcnt += len(rules)

        print(f"Summary for {train_and_wal_size}:{train_and_wal_size}:{1728 - 2 * train_and_wal_size}:\n")
        print(f"rules_cnt: {rcnt / gen_times}\n")
        print(f"accuracy: {acc / gen_times}\n\n")
