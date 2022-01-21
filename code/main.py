from test_utilities import *
from file_utiities import *
from aq_utilities import *
from rule import *

### Global parameters
debug_on = False
custom_neg_seed = False
best_complexes_param = 5
minimize_rules_cnt_param = 0


if __name__ == "__main__":

    for i in [400, 600, 800, 1000, 1200, 1400, 1600]:
        acc = 0
        rcnt = 0
        gen_times = 10
        for j in range(gen_times):
            divide_file_randomly_on_two_parts("../data/car.data", i)
            examples = read_examples("../data/car.dataextracted")
            examples, T = get_rand_examples(examples, i/2)
            examples, W = get_rand_examples(examples, i/2)
            test = read_examples("../data/car.datarest")

            rules = generate_rules(T, W)
            acc += test_rules(rules, test)
            rcnt += len(rules)

        print(f"Summary for {i/2}:{i/2}:{1728-i}:")
        print(f"rules_cnt: {rcnt / gen_times}\n")
        print(f"accuracy: {acc / gen_times}\n\n")

