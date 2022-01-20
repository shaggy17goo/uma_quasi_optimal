from test_utilities import *
from file_utiities import *
from aq_utilities import *
from rule import *

best_complexes_param = 5

if __name__ == "__main__":
    acc = 0
    rcnt = 0
    gen_times = 10
    for j in range(gen_times):
        divide_file_randomly_on_two_parts("../data/car.data", 1000)
        examples = read_examples("../data/car.dataextracted")
        examples, T = get_rand_examples(examples, 500)
        examples, W = get_rand_examples(examples, 500)
        test = read_examples("../data/car.datarest")

        rules = generate_rules(T, W)
        acc += test_rules(rules, test)
        rcnt += len(rules)

    print(f"Summary for {best_complexes_param}:")
    print(f"rules_cnt: {rcnt / gen_times}\n")
    print(f"accuracy: {acc / gen_times}\n\n")
