from test_utilities import *
from file_utiities import *
from aq_utilities import *
from rule import *

### Global parameters
debug_on = False
custom_neg_seed = False
best_complexes_param = 5
minimize_rules_cnt_param = 0
train_and_wal_size = 700


if __name__ == "__main__":
    file = open("output.txt", "w")
    file.write("test output")
    best_complexes_param = 5
    for i in [400, 600, 800, 1000, 1200, 1400, 1600]:
        acc = 0
        rcnt = 0
        gen_times = 100
        for j in range(gen_times):
            divide_file_randomly_on_two_parts("../data/car.data", i)
            examples = read_examples("../data/car.dataextracted")
            examples, T = get_rand_examples(examples, i / 2)
            examples, W = get_rand_examples(examples, i / 2)
            test = read_examples("../data/car.datarest")

            rules = generate_rules(T, W)
            acc += test_rules(rules, test)
            rcnt += len(rules)

        print(f"Summary for {i / 2}:{i / 2}:{1728 - i}:")
        print(f"rules_cnt: {rcnt / gen_times}\n")
        print(f"accuracy: {acc / gen_times}\n\n")
        file.write(f"Summary for {i / 2}:{i / 2}:{1728 - i}:")
        file.write(f"rules_cnt: {rcnt / gen_times}\n")
        file.write(f"accuracy: {acc / gen_times}\n\n")

    print("####################################################################")
    file.write("####################################################################")

    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
        best_complexes_param = i
        acc = 0
        rcnt = 0
        gen_times = 100
        for j in range(gen_times):
            divide_file_randomly_on_two_parts("../data/car.data", train_and_wal_size*2)
            examples = read_examples("../data/car.dataextracted")
            examples, T = get_rand_examples(examples, train_and_wal_size)
            examples, W = get_rand_examples(examples, train_and_wal_size)
            test = read_examples("../data/car.datarest")

            rules = generate_rules(T, W)
            acc += test_rules(rules, test)
            rcnt += len(rules)

        print(f"Summary for {best_complexes_param}:")
        print(f"rules_cnt: {rcnt / gen_times}\n")
        print(f"accuracy: {acc / gen_times}\n\n")
        file.write(f"Summary for {best_complexes_param}:")
        file.write(f"rules_cnt: {rcnt / gen_times}\n")
        file.write(f"accuracy: {acc / gen_times}\n\n")

    print("####################################################################")
    file.write("####################################################################")

    best_complexes_param = 5
    for i in [1, 2]:
        if i == 1:
            custom_neg_seed = True
        else:
            custom_neg_seed = False
        acc = 0
        rcnt = 0
        gen_times = 100
        for j in range(gen_times):
            divide_file_randomly_on_two_parts("../data/car.data", train_and_wal_size*2)
            examples = read_examples("../data/car.dataextracted")
            examples, T = get_rand_examples(examples, train_and_wal_size)
            examples, W = get_rand_examples(examples, train_and_wal_size)
            test = read_examples("../data/car.datarest")

            rules = generate_rules(T, W)
            acc += test_rules(rules, test)
            rcnt += len(rules)

        if i == 1:
            print(f"Summary for custom neg seed:")
            file.write(f"Summary for custom neg seed:")
        else:
            print(f"Summary for random neg seed:")
            file.write(f"Summary for random neg seed:")

        print(f"rules_cnt: {rcnt / gen_times}\n")
        print(f"accuracy: {acc / gen_times}\n\n")
        file.write(f"rules_cnt: {rcnt / gen_times}\n")
        file.write(f"accuracy: {acc / gen_times}\n\n")

    file.close()
