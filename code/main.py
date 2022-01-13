from utilities import *
from rule import *

if __name__ == "__main__":
    while 1:
        examples = read_examples("../data/car.data")
        examples, T = get_rand_examples(examples, 500)
        examples, W = get_rand_examples(examples, 500)
        test = examples

        rules = []
        R = deepcopy(T)

        while len(R) != 0:
            k = aq_specialization(R, W)
            d = get_prevail_class(k, R)
            rules.append(Rule(k, d))
            R = remove_from_set(k, R)
            W = remove_from_set(k, W)


        save_rules(rules)

        #rules = read_rules("rules/rules.2.pkl")
        #print_rules(rules)
        #test_rules(rules, test)




