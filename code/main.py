from file_utiities import *
from aq_utilities import *
from rule import *

if __name__ == "__main__":
#    '''

    examples = read_examples("../data/car.data.tren_wal")
    examples, T = get_rand_examples(examples, 700)
    examples, W = get_rand_examples(examples, 700)

    rules = generate_rules(T, W)
    save_rules(rules)
#        '''

#    test = read_examples("../data/car.data")


#    for i in range(1, 31):
#        rules = read_rules(f"rules/rules.{i}.pkl")
#        #print_rules(rules)
#        test_rules(rules, test)
#        print("\n\n\n\n\n")
